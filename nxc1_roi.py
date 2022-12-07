from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor, QMouseEvent
from PySide6.QtCore import Slot, Qt

from lib.mywidget import MyWidget
import skimage.io
import numpy as np
import cv2
import sys


class NxC1_RoI(MyWidget):
    def __init__(self) -> None:
        super().__init__()
        self.origins = np.empty(0)
        self.origin = np.empty(0)
        self.xx, self.yy = 0, 0
        self.d = 0
        self.cnt = 0

    def on_mouse(self, type: int, event: QMouseEvent):
        if type == 0 and event.buttons() == Qt.MouseButton.LeftButton:
            self.xx, self.yy = event.x(), event.y()
            self.printf(f'Anchor, ({self.xx}, {self.yy})')
        elif type == 2 and event.buttons() == Qt.MouseButton.LeftButton:
            self.d = max(event.y() - self.yy, event.x() - self.xx)
            img = self.origin.copy()
            cv2.rectangle(img, (self.xx, self.yy), (self.xx + self.d, self.yy + self.d), (0, 255, 0), 1)
            self.imshow(img)
        elif type == 1:
            pass
        else:
            self.printf(f'{type} {event.buttons()}')

    def openfile(self):
        path, _ = QFileDialog().getOpenFileName()
        self.origins = skimage.io.imread(path)
        self.printf(self.origins.shape)
        cv2.namedWindow('image')
        on_pos(0)

    def savefile(self):
        self.cnt += 1
        cv2.imwrite(f'{self.cnt}.jpg', self.origin[self.yy:self.yy + self.d, self.xx:self.xx + self.d] / 256)
        self.printf(f'{self.d}, {self.origin.shape}')


def on_pos(x):
    img = cfg.origins[x]
    cv2.normalize(img, img, 0, 65535, cv2.NORM_MINMAX)
    cfg.origin = cv2.resize(img, (0, 0), img, 0.5, 0.5)
    draw()


def draw():
    cfg = Cfg()
    img = cfg.origin.copy()
    cv2.rectangle(img, (cfg.xx, cfg.yy), (cfg.xx + cfg.d, cfg.yy + cfg.d), (0, 255, 0), 2)
    cv2.imshow('image', img)
