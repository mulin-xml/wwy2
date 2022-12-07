from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor, QMouseEvent
from PySide6.QtCore import Slot, Qt
from lib.mywidget import MyWidget
import numpy as np
import cv2
import sys


class N1C3_RoI(MyWidget):
    def __init__(self) -> None:
        super().__init__()
        self.origin = None
        self.xx, self.yy = 0, 0
        self.d = 0

    def on_mouse(self, type: int, event: QMouseEvent):
        if type == 0 and event.buttons() == Qt.MouseButton.LeftButton:
            self.xx, self.yy = event.x(), event.y()
            self.printf(f'Anchor, ({self.xx}, {self.yy})')
        elif type == 2 and event.buttons() == Qt.MouseButton.LeftButton:
            self.d = max(event.y() - self.yy, event.x() - self.xx)
            img = self.origin.copy()
            cv2.rectangle(img, (self.xx, self.yy), (self.xx + self.d, self.yy + self.d), (0, 255, 0), 2)
            self.imshow(img)
        elif type == 1:
            pass
        else:
            self.printf(type, event.buttons())

    def openfile(self):
        path, _ = QFileDialog().getOpenFileName()
        self.origin = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
        self.imshow(self.origin)

    def on_save(self):
        for i in range(3):
            j = np.zeros((self.d, self.d, 3))
            j[:, :, i] = self.origin[self.yy:self.yy + self.d, self.xx:self.xx + self.d, i]
            cv2.imwrite(f'{i}.jpg', j)
        cv2.imwrite('3.jpg', self.origin[self.yy:self.yy + self.d, self.xx:self.xx + self.d, :])
        self.printf(f'{self.d}, {self.origin.shape}')
        cv2.destroyAllWindows()
