from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QButtonGroup
from PySide6.QtCore import QPoint, QMimeData, QUrl, QMetaObject, Slot
from PySide6.QtGui import QImage, QPixmap
from PIL import Image, ImageDraw, ImageFont
from typing import TYPE_CHECKING
from datetime import datetime

import numpy as np
import tifffile
import cv2
import os

if TYPE_CHECKING:
    from uic.main_dialog_logic import MainWindow


class ColorPara:
    def __init__(self) -> None:
        self.min = 0
        self.max = 255


class RoI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.img: np.ndarray = None
        self.stk: np.ndarray = None

        self.anchor = QPoint()
        self.d = 0

        self.c_para = [ColorPara(), ColorPara(), ColorPara(), ColorPara()]

    def setupUi(self, ui):
        self.ui: MainWindow = ui

        self.colorChannel = QButtonGroup(self)
        for child in self.ui.tab1ChannelGroup.children():
            if child.inherits('QRadioButton'):
                self.colorChannel.addButton(child)
        self.colorChannel.idClicked.connect(self.when_radio_clicked)

        self.colorPara = QButtonGroup(self)
        for child in self.ui.tab1ParaGroup.children():
            if child.inherits('QRadioButton'):
                self.colorPara.addButton(child)
        self.colorPara.idClicked.connect(self.when_radio_clicked)

        QMetaObject.connectSlotsByName(self)

    def when_radio_clicked(self):
        self.ui.tab1BCBar.setDisabled(self.colorChannel.checkedId() >= -2 and self.colorPara.checkedId() == -3)
        self.ui.tab1SliderMin.setValue(self.current_para.min)
        self.ui.tab1SliderMax.setValue(self.current_para.max)
        self.render_img()

    @Slot(int)
    def on_tab1SliderMin_valueChanged(self, value):
        self.current_para.min = value
        self.render_img()

    @Slot(int)
    def on_tab1SliderMax_valueChanged(self, value):
        self.current_para.max = value
        self.render_img()

    @property
    def selected_channel(self):
        return self.colorChannel.checkedId() + 5

    @property
    def current_para(self):
        return self.c_para[3] if self.colorPara.checkedId() == -2 else self.c_para[self.selected_channel]

    @Slot()
    def on_tab1SaveButton_clicked(self):
        cb = QApplication.clipboard()
        cb.clear()
        urls = []

        s1 = slice(self.anchor.y(), self.anchor.y() + self.d)
        s2 = slice(self.anchor.x(), self.anchor.x() + self.d)
        _, w, c = self.img.shape
        for i in range(c):
            img = np.zeros((self.d, self.d, c))
            img[:, :, i] = self.img[s1, s2, i]
            urls.append(self.__imwrite(img, w))
        if c > 1:
            urls.append(self.__imwrite(self.img[s1, s2], w))

        mimedata = QMimeData()
        mimedata.setUrls(urls)
        cb.setMimeData(mimedata)
        self.ui.printf(f'Src size{self.img.shape}', f'RoI width: {self.d}')

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

    @Slot()
    def on_tab1OpenImgButton_clicked(self):
        path, _ = QFileDialog().getOpenFileName()
        path: str
        if not path:
            self.ui.printf('User presses cancel.')
            return
        # Read image file.
        if path.endswith('.stk'):
            self.ui.tab1ImgSlider.setEnabled(True)
            self.stk = tifffile.imread(path)
            self.ui.tab1ImgSlider.setRange(0, self.stk.shape[0] - 1)
            self.ui.tab1ImgSlider.setValue(0)
            img = self.stk[0]
        else:
            self.ui.tab1ImgSlider.setEnabled(False)
            img = np.array(Image.open(path))
        self.img_preprocess(img)

    @Slot(int)
    def on_tab1ImgSlider_valueChanged(self, value):
        self.img_preprocess(self.stk[value], is_same_stack=True)

    def img_preprocess(self, img: np.ndarray, is_same_stack=False):
        '''
        目标图像切换时的预处理
        ---
        在重新选择图片和滚动条变化时触发
        '''
        if img.itemsize == 2:
            # 16位图像转8位
            img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
            img = img.astype(np.uint8)

        if is_same_stack or self.colorChannel.checkedId() >= -2:
            # Select multi channel.
            self.ui.printf('multi')
            self.img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        else:
            # Select single channel.
            if img.ndim == 2:  # 插入的是单通道图像
                self.ui.printf('single')
                if self.img is None or self.img.shape[:2] != img.shape:
                    self.img = np.zeros((img.shape[0], img.shape[1], 3))
                self.img[:, :, self.selected_channel] = img
            elif img.ndim == 3:  # 插入的是多通道图像
                self.ui.printf('当前通道不支持插入多通道图像')
                return
            else:  # 异常路径
                self.ui.printf(f'Error: img.shape is {img.shape}.')
                return
        self.render_img()

    def build_hist(self, img: np.ndarray) -> np.ndarray:
        freq, _ = np.histogram(img.ravel(), bins=256, range=(0, 256))
        hist = np.zeros((256, 256, 3), dtype=np.uint8)
        for i in range(256):
            hist[255 - int(freq[i] / freq.max() * 255):, i, :] = 255
        return hist

    def render_img(self):
        '''
        渲染图像
        ---
        在目标图像切换、选区变化、对比度和选择通道变化时触发
        按照新值重新渲染通道、对比度和选区
        '''
        if self.img is None:
            return

        if self.colorChannel.checkedId() >= -2:
            if self.colorPara.checkedId() == -2:
                hist = self.build_hist(img)
                img = cv2.normalize(self.img, None, self.c_para[3].min, self.c_para[3].max, cv2.NORM_MINMAX)
            else:
                img = np.empty(self.img.shape, dtype=np.uint8)
                for i in range(3):
                    img[:, :, i] = cv2.normalize(self.img[:, :, i], None, self.c_para[i].min, self.c_para[i].max, cv2.NORM_MINMAX)
        else:
            img = np.zeros(self.img.shape, dtype=np.uint8)
            hist = self.build_hist(img)
            img[:, :, self.selected_channel] = cv2.normalize(self.img[:, :, self.selected_channel], None, self.current_para.min,
                                                             self.current_para.max, cv2.NORM_MINMAX)

        cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), (255, 255, 0), 4)
        self.ui.tab1GV.imshow(img)

        h, w = hist.shape
        self.ui.tab1Hist.setPixmap(QPixmap.fromImage(QImage(hist, w, h, w * 3, QImage.Format.Format_BGR888)))

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
            ImageDraw.Draw(tmp_img).text(
                xy=(dst_width - margin - length, int(dst_height - margin * 1.3 - fontsize)),
                text=f'{self.ui.to_edit.text()}\u03bcm',
                font=ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', fontsize),
                fill=(255,) * img.shape[2])
            dst = np.array(tmp_img)
        name = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")}.png'
        cv2.imwrite(name, dst)
        return QUrl.fromLocalFile(os.path.join(os.getcwd(), name))
