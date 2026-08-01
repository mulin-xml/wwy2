from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QMetaObject, Slot, QPoint
from PySide6.QtGui import QImage, QPixmap
from typing import TYPE_CHECKING
from PIL import Image

import numpy as np
import math
import cv2

if TYPE_CHECKING:
    from uic.main_dialog_logic import MainWindow


class Watershed(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.img: np.ndarray = None
        self.hist = np.zeros((256, 256, 3), dtype=np.uint8)
        self.rs: np.ndarray = None

        self.idx = 0
        self.marks = None

    def setupUi(self, ui):
        self.ui: MainWindow = ui

        QMetaObject.connectSlotsByName(self)

    @Slot(int, QPoint)
    def on_tab3GV_mouseSig(self, action: int, pos: QPoint):
        if action == 0:
            self.idx += 1
        elif action == 1:
            self.marks[pos.y(), pos.x()] = self.idx
            self.ui.printf(action, pos,self.idx)
            self.render_img()
        else:
            self.ui.printf(action, pos)

    @Slot()
    def on_tab3OpenImg_clicked(self):
        path, _ = QFileDialog().getOpenFileName()
        path: str
        if not path:
            self.ui.printf('User presses cancel.')
            return
        # Read image file.
        img = np.array(Image.open(path))
        self.img = img if img.ndim == 2 else cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)[:,:,None]  # shape(H, W)
        self.ui.printf(self.img.shape)

        self.hist *= 0
        freq, _ = np.histogram(self.img[:, :].ravel(), bins=256, range=(0, 256))
        for j in range(256):
            self.hist[255 - int(freq[j] / freq.max() * 255):, j, :] = 255
        self.show_hist()
        # self.render_img()
        self.marks = np.zeros(self.img.shape[:2], dtype=np.int32)
        self.ui.tab3GV.imshow(self.img)

    def render_img(self):
        if self.img is None:
            return

        img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)

        contours, hierarchy = cv2.findContours(self.marks, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        marks = np.zeros(img.shape[:2], np.int32)
        imageContours = np.zeros(img.shape[:2], np.uint8)
        # 轮廓颜色
        compCount = 0
        index = 0
        for index in range(len(contours)):
    
            # 对marks进行标记，对不同区域的轮廓使用不同的亮度绘制，相当于设置注水点，有多少个轮廓，就有多少个注水点
            # 图像上不同线条的灰度值是不同的，底部略暗，越往上灰度越高
            marks = cv2.drawContours(marks, contours, index, (index, index, index), 1, 8, hierarchy)
        markerShows = cv2.convertScaleAbs(marks)
        # 使用分水岭算法
        marks = cv2.watershed(img, marks)
        afterWatershed = cv2.convertScaleAbs(marks)
        ###分水岭算法之后,让水漫起来,并且把堤坝即分水岭绘制为绿色
        img[marks == -1] = [ 0, 255, 0]


        self.ui.tab3GV.imshow(img)

        # rs = np.array(rs)
        # self.rs = rs
        # self.ui.tab2Num.setText(f'{rs.size}')
        # self.ui.tab2Min.setText(f'{rs.min():.2f}')
        # self.ui.tab2Max.setText(f'{rs.max():.2f}')
        # self.ui.tab2Mean.setText(f'{rs.mean():.2f}')
        # self.ui.tab2Mid.setText(f'{np.percentile(rs, 50):.2f}')
        # self.ui.printf(f'num: {rs.size}, min: {rs.min():.2f}, max: {rs.max():.2f}, mean: {rs.mean():.2f}, mid: {np.percentile(rs, 50):.2f}')

    def show_hist(self):
        h, w, c = self.hist.shape
        self.ui.tab2Hist.setPixmap(QPixmap.fromImage(QImage(self.hist, w, h, w * c, QImage.Format.Format_BGR888)))

    # @Slot()
    # def on_tab3ExportButton_clicked(self):
    #     if self.rs is None:
    #         self.ui.printf('还没有结果')
    #         return
    #     path, _ = QFileDialog().getSaveFileName(dir='rs.txt')
    #     if not path:
    #         self.ui.printf('User presses cancel.')
    #     else:
    #         np.savetxt(path, self.rs, fmt='%.3f')
