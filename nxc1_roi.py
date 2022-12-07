from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor, QMouseEvent
from PySide6.QtCore import Slot, Qt, QPoint

from lib.mywidget import MyWidget
import numpy as np
import cv2
import sys
import tifffile


class NxC1_RoI(MyWidget):
    def __init__(self) -> None:
        super().__init__()
        self.origins = np.empty(0)
        self.origin = np.empty(0)
        self.anchor = QPoint()
        self.d = 0
        self.cnt = 0

    def on_mouse(self, type: int, pos: QPoint):
        if type == 0:
            self.anchor = pos
            self.printf(f'Anchor, ({self.xx}, {self.yy})')
        elif type == 2:
            d = pos - self.anchor
            self.d = max(d.x(), d.y())
            self.draw()
        else:
            pass

    def openfile(self):
        path, _ = QFileDialog().getOpenFileName()
        self.origins = tifffile.imread(path)
        self.printf(f'{self.origins.shape}')
        self.on_pos(0)

    def savefile(self):
        self.cnt += 1
        cv2.imwrite(f'{self.cnt}.jpg', self.origin[self.yy:self.yy + self.d, self.xx:self.xx + self.d] / 256)
        self.printf(f'{self.d}, {self.origin.shape}')

    def on_pos(self, x):
        img = self.origins[x]
        cv2.normalize(img, self.origin, 0, 65535, cv2.NORM_MINMAX)
        self.draw()

    def draw(self):
        img = self.origin.copy()
        cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), 255, 2)
        self.imshow(img)
