from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QPoint
from PySide6.QtGui import QImage
from lib.mywidget import MyWidget

import numpy as np
import cv2


class N1C3_RoI(MyWidget):
    def __init__(self) -> None:
        super().__init__()
        self.origin = np.empty(0)
        self.anchor = QPoint()
        self.d = 0

    def on_mouse(self, action: int, pos: QPoint):
        if action == 0:
            self.anchor = pos
        elif action == 2:
            d = pos - self.anchor
            self.d = max(d.x(), d.y())
            img = self.origin.copy()
            cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), (0, 255, 0), 2)
            self.imshow(img)
        else:
            self.printf(action, pos)

    def openfile(self):
        path, _ = QFileDialog().getOpenFileName()
        self.origin = cv2.imdecode(np.fromfile(path, dtype=np.uint8), flags=cv2.IMREAD_UNCHANGED)
        self.imshow(self.origin, form=QImage.Format.Format_BGR888)

    def savefile(self):
        s1 = slice(self.anchor.y(), self.anchor.y() + self.d)
        s2 = slice(self.anchor.x(), self.anchor.x() + self.d)
        for i in range(3):
            img = np.zeros((self.d, self.d, 3))  # 保存为3通道图像
            img[:, :, i] = self.origin[s1, s2, i]
            cv2.imwrite(f'{i}.jpg', img)
        cv2.imwrite('3.jpg', self.origin[s1, s2])
        self.printf(self.d, self.origin.shape)
