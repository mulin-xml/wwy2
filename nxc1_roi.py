from PySide6.QtWidgets import QFileDialog, QSlider
from PySide6.QtGui import QImage
from PySide6.QtCore import QPoint
from lib.mywidget import MyWidget
from typing import cast
import numpy as np
import tifffile
import cv2


class NxC1_RoI(MyWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = QImage.Format.Format_Grayscale16
        self.origins = np.empty(0)
        self.origin = np.empty(0)
        self.anchor = QPoint()
        self.d = 0
        self.cnt = 0

    def init(self):
        self.slider = cast(QSlider, self.findChild(QSlider))
        self.slider.valueChanged.connect(self.on_pos)
        return super().init()

    def on_mouse(self, action: int, pos: QPoint):
        if action == 0:
            self.anchor = pos
        elif action == 1:
            d = pos - self.anchor
            self.d = max(d.x(), d.y())
            self.draw()
        else:
            self.printf(action, pos)
        return super().on_mouse(action, pos)

    def openfile(self):
        path, _ = QFileDialog().getOpenFileName()
        if path:
            self.cnt = 0
            self.origins = tifffile.imread(path)
            self.printf(self.origins.shape)
            self.slider.setRange(0, self.origins.shape[0] - 1)
            self.slider.setValue(0)
            self.on_pos(0)

    def savefile(self):
        self.cnt += 1
        s1 = slice(self.anchor.y(), self.anchor.y() + self.d)
        s2 = slice(self.anchor.x(), self.anchor.x() + self.d)
        cv2.imwrite(f'{self.cnt}.jpg', self.origin[s1, s2] / 256)
        self.printf(self.d, self.origin.shape)

    def on_pos(self, x):
        img = self.origins[x]
        self.origin = cv2.normalize(img, None, 0, 65535, cv2.NORM_MINMAX)
        self.draw()
        self.printf(x)

    def draw(self):
        img = self.origin.copy()
        cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), 255, 2)
        self.imshow(img[:, :, None])
