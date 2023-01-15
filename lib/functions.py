from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QPoint, QMimeData, QUrl
from typing import TYPE_CHECKING
from abc import abstractmethod
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

import numpy as np
import cv2
import os

if TYPE_CHECKING:
    from main import MainWindow


class BaseFunction:
    def __init__(self, ui) -> None:
        self.ui: MainWindow = ui

    @property
    def img(self) -> np.ndarray:
        return self.ui.img

    @abstractmethod
    def on_mouse(self, action: int, pos: QPoint): ...

    @abstractmethod
    def render_img(self): ...

    def printf(self, *value):
        self.ui.printf(*value)

    def imshow(self, img):
        self.ui.gv.imshow(img)


class RoI(BaseFunction):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.anchor = QPoint()
        self.d = 0

        # 手动信号槽
        self.ui.pushButton.clicked.connect(self.savefile)

    def render_img(self):
        img = self.img.copy()
        cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), (255, 255, 0), 4)
        self.imshow(img)
        return super().render_img()

    def on_mouse(self, action: int, pos: QPoint):
        if action == 0:
            self.anchor = pos
        elif action == 1:
            d = pos - self.anchor
            self.d = max(d.x(), d.y())
            self.render_img()
        else:
            self.printf(action, pos)

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

    def savefile(self):
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
        self.printf(f'Src size{self.img.shape}', f'RoI width: {self.d}')


class CircleCounter(BaseFunction):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.circles = []

        # 手动信号槽
        self.ui.pushButton_2.clicked.connect(self.calc)

    def render_img(self):
        img = self.img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # 灰度图
        for i in self.circles:  # 遍历矩阵的每一行的数据
            img = cv2.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 0), 1)
            img = cv2.circle(img, (int(i[0]), int(i[1])), 1, (255, 255, 0), -1)
        self.imshow(img)
        return super().render_img()

    def calc(self):
        self.printf('计算中 大约耗时10秒 请耐心等待')
        self.circles = cv2.HoughCircles(self.img.squeeze(), cv2.HOUGH_GRADIENT, 1, 40, param1=50, param2=20, minRadius=0, maxRadius=100).squeeze()
        self.printf(self.circles)
        self.render_img()
