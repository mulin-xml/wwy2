from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QPoint, QMimeData, QUrl, QMetaObject, Slot, Qt
from typing import TYPE_CHECKING, Optional
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

import tifffile
import numpy as np
import cv2
import os

if TYPE_CHECKING:
    from uic.main_dialog_logic import MainWindow


class RoI(QWidget):

    def __init__(self, parent: Optional[QWidget] = ..., f: Qt.WindowType = ...) -> None:
        super().__init__()

        self.anchor = QPoint()
        self.d = 0

        self.img: np.ndarray = None
        self.stk: np.ndarray = None

    def setupUi(self, ui):
        self.ui: MainWindow = ui
        QMetaObject.connectSlotsByName(self)

    def render_img(self):
        if self.img is None:
            return
        img = self.img.copy()
        cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), (255, 255, 0), 4)
        self.ui.tab1GV.imshow(img)

    @Slot()
    def on_tab1OpenImgButton_clicked(self):
        path, _ = QFileDialog().getOpenFileName()
        if not path:
            self.ui.printf('User presses cancel.')
            return
        path: str
        if path.endswith('.stk'):
            self.ui.tab1ImgSlider.setEnabled(True)
            self.stk = tifffile.imread(path)
            self.ui.tab1ImgSlider.setRange(0, self.stk.shape[0] - 1)
            self.img = self.stk[0]
        else:
            self.ui.tab1ImgSlider.setEnabled(False)
            self.img = np.array(Image.open(path))
        self.ui.tab1ImgSlider.setValue(0)
        self.img_preprocess()

    @Slot(int)
    def on_tab1ImgSlider_valueChanged(self, value):
        self.img = self.stk[value]
        self.img_preprocess()
        self.render_img()

    @Slot(int, QPoint)
    def on_tab1GV_mouseSig(self, action: int, pos: QPoint):
        if action == 0:
            self.anchor = pos
        elif action == 1:
            d = pos - self.anchor
            self.d = max(d.x(), d.y())
            self.render_img()
        else:
            self.ui.printf(action, pos)

    def img_preprocess(self):
        '''
        目标图像切换时的预处理
        '''
        if self.img.itemsize == 2:
            # 16位图像转8位
            self.img = cv2.normalize(self.img, None, 0, 255, cv2.NORM_MINMAX)
            self.img = self.img.astype(np.uint8)

        if self.img.ndim == 2:  # 单通道图像
            self.img = self.img[:, :, None]
        elif self.img.ndim == 3:  # 3通道图像
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        else:
            self.ui.printf(f'Error: img.shape is {self.img.shape}.')
        self.ui.tab1GV.imshow(self.img)
        # self.hist.update(self.img)

    def __imwrite(self, img: np.ndarray, origin_width=None) -> QUrl:
        width = img.shape[1]
        if origin_width is None:
            origin_width = width
        rate = 1000 / width
        dst = cv2.resize(img, None, fx=rate, fy=rate)  # 宽度对齐1000px
        dst_width, dst_height = dst.shape[1], dst.shape[0]

        if self.ui.line_check.isChecked():
            margin = 45
            fontsize = 50
            length = int(origin_width / float(self.ui.from_edit.text()) * float(self.ui.to_edit.text()) * rate)
            cv2.line(dst, (dst_width - margin - length, dst_height - margin), (dst_width - margin, dst_height - margin), [255] * 3, 8)
            tmp_img = Image.fromarray(np.uint8(dst))
            font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', fontsize)
            ImageDraw.Draw(tmp_img).text((dst_width - margin - length, int(dst_height - margin * 1.3 - fontsize)), f'{self.ui.to_edit.text()}\u03bcm', font=font, fill=(255,) * img.shape[2])
            dst = np.array(tmp_img)
        name = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")}.png'
        cv2.imwrite(name, dst)
        return QUrl.fromLocalFile(os.path.join(os.getcwd(), name))

    @Slot()
    def on_tab1SaveButton_clicked(self):
        cb = QApplication.clipboard()
        cb.clear()
        mimedata = QMimeData()
        urls = []

        s1 = slice(self.anchor.y(), self.anchor.y() + self.d)
        s2 = slice(self.anchor.x(), self.anchor.x() + self.d)
        h, w, c = self.img.shape
        for i in range(c):
            img = np.zeros((self.d, self.d, c))
            img[:, :, i] = self.img[s1, s2, i]
            urls.append(self.__imwrite(img, w))
        if c > 1:
            urls.append(self.__imwrite(self.img[s1, s2], w))
        mimedata.setUrls(urls)
        cb.setMimeData(mimedata)
        self.ui.printf(f'Src size{self.img.shape}', f'RoI width: {self.d}')
