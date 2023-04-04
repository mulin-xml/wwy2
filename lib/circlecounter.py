from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QMetaObject, Slot
from PySide6.QtGui import QImage, QPixmap
from typing import TYPE_CHECKING
from PIL import Image

import numpy as np
import math
import cv2

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
        self.show_hist()
        self.render_img()

    def render_img(self):
        if self.img is None:
            return

        gray = self.img
        img3 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        # kernel = np.ones((2, 2), np.uint8)  # 进行腐蚀膨胀操作
        # erosion = cv2.erode(gray, kernel, iterations=5)  # 膨胀
        # dilation = cv2.dilate(erosion, kernel, iterations=5)  # 腐蚀
        _, binary = cv2.threshold(gray, self.ui.tab2BrightThres.value(), 255, cv2.THRESH_BINARY)
        # thresh1 = cv2.GaussianBlur(thresh1, (3, 3), 0)  # 高斯滤波
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [i for i in contours if cv2.contourArea(i) >= self.ui.tab2AreaThres.value()]
        cv2.drawContours(img3, contours, -1, (0, 255, 0), 1)

        rs = []
        for contour in contours:
            area = cv2.contourArea(contour)
            (x, y), _ = cv2.minEnclosingCircle(contour)
            r2 = math.sqrt(area / math.pi)
            cv2.putText(img3, f'{r2:.1f}', (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 255), 1)
            rs.append(r2)
        self.ui.tab2GV.imshow(img3)
        rs = np.array(rs)
        self.ui.printf(f'num: {rs.size}, min: {rs.min():.2f}, max: {rs.max():.2f}, mean: {rs.mean():.2f}, mid: {np.percentile(rs, 50):.2f}')

    def show_hist(self):
        h, w, c = self.hist.shape
        self.ui.tab2Hist.setPixmap(QPixmap.fromImage(QImage(self.hist, w, h, w * c, QImage.Format.Format_BGR888)))

    @Slot(int)
    def on_tab2BrightThres_valueChanged(self, value):
        self.render_img()

    @Slot(int)
    def on_tab2AreaThres_valueChanged(self, value):
        self.render_img()

    @Slot()
    def on_tab2CntButton_clicked(self):
        pass
