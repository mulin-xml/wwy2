from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot
import numpy as np
import cv2
import sys


class Cfg:
    origin = None
    xx, yy = 0, 0
    d = 0


class MyWidget(QWidget):
    def __init__(self, parent, f) -> None:
        super().__init__(parent, f)
        self.logger = self.parent().parent().parent().textEdit


class N1C3_RoI(MyWidget):
    def on_mouse(self, event, x, y, flags: int, cfg: Cfg):
        if event == cv2.EVENT_LBUTTONDOWN:
            cfg.xx, cfg.yy = x, y
            self.printf(f'Anchor, ({cfg.xx}, {cfg.yy})')
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            cfg.d = max(y - cfg.yy, x - cfg.xx)
            img = cfg.origin.copy()
            cv2.rectangle(img, (cfg.xx, cfg.yy), (cfg.xx + cfg.d, cfg.yy + cfg.d), (0, 255, 0), 2)
            cv2.imshow('image', img)

    @Slot()
    def button_clicked(self):
        path, _ = QFileDialog().getOpenFileName()
        self.printf(path)
        cfg = Cfg()
        cfg.origin = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.namedWindow('image')
        cv2.imshow('image', cfg.origin)
        cv2.setMouseCallback('image', self.on_mouse, cfg)
        while cv2.waitKey(1) != ord('q'):
            pass
        for i in range(3):
            j = np.zeros((cfg.d, cfg.d, 3))
            j[:, :, i] = cfg.origin[cfg.yy:cfg.yy + cfg.d, cfg.xx:cfg.xx + cfg.d, i]
            cv2.imwrite(f'{i}.jpg', j)
        cv2.imwrite('3.jpg', cfg.origin[cfg.yy:cfg.yy + cfg.d, cfg.xx:cfg.xx + cfg.d, :])
        self.printf(f'{cfg.d}, {cfg.origin.shape}')
        cv2.destroyAllWindows()
