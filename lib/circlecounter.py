from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QButtonGroup
from PySide6.QtCore import QPoint, QMimeData, QUrl, QMetaObject, Slot
from PIL import Image
from PySide6.QtGui import QImage, QPixmap
from typing import TYPE_CHECKING
from datetime import datetime

import numpy as np
import cv2
import os

if TYPE_CHECKING:
    from uic.main_dialog_logic import MainWindow


class CircleCounter(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.img: np.ndarray = None
        self.hist = np.zeros((256, 256, 3), dtype=np.uint8)

    def setupUi(self, ui):
        self.ui: MainWindow = ui

        QMetaObject.connectSlotsByName(self)
        self.show_hist()

    @Slot()
    def on_tab2OpenImgButton_clicked(self):
        path, _ = QFileDialog().getOpenFileName()
        path: str
        if not path:
            self.ui.printf('User presses cancel.')
            return
        # Read image file.
        img = np.array(Image.open(path))
        self.img = img if img.ndim == 2 else cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # shape(H, W)
        self.ui.printf(self.img.shape)

        self.hist *= 0
        freq, _ = np.histogram(self.img[:, :].ravel(), bins=256, range=(0, 256))
        for j in range(256):
            self.hist[255 - int(freq[j] / freq.max() * 255):, j, :] = 255
        self.render_img()

    def render_img(self):
        '''
        渲染图像
        ---
        在目标图像切换、选区变化、对比度和选择通道变化时触发
        按照新值重新渲染通道、对比度和选区
        '''
        if self.img is None:
            return

        self.ui.tab2GV.imshow(self.img[:, :, None])
        self.show_hist()

    def show_hist(self):
        h, w, c = self.hist.shape
        hist = self.hist.copy()
        self.ui.tab2Hist.setPixmap(QPixmap.fromImage(QImage(hist, w, h, w * c, QImage.Format.Format_BGR888)))
