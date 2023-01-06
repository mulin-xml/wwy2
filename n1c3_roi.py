from PySide6.QtWidgets import QFileDialog, QApplication
from PySide6.QtCore import QPoint, QMimeData, QUrl
from PySide6.QtGui import QImage
from lib.mywidget import MyWidget

import numpy as np
import cv2


class N1C3_RoI(MyWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = QImage.Format.Format_BGR888
        self.origin = np.empty(0)
        self.anchor = QPoint()
        self.d = 0

    def on_mouse(self, action: int, pos: QPoint):
        if action == 0:
            self.anchor = pos
        elif action == 1:
            d = pos - self.anchor
            self.d = max(d.x(), d.y())
            img = self.origin.copy()
            cv2.rectangle(img, self.anchor.toTuple(), (self.anchor.x() + self.d, self.anchor.y() + self.d), (255, 255, 0), 2)
            self.imshow(img)
        else:
            self.printf(action, pos)

    def openfile(self):
        path, _ = QFileDialog().getOpenFileName()
        if path:
            self.origin: np.ndarray = cv2.imdecode(np.fromfile(path, dtype=np.uint8), flags=cv2.IMREAD_UNCHANGED)
            if self.origin.ndim == 2:
                self.origin = self.origin[:, :, None]
                self.form = QImage.Format.Format_Grayscale8
            else:
                self.form = QImage.Format.Format_BGR888
            self.imshow(self.origin)
            self.printf(f'Src size{self.origin.shape}')

    def savefile(self):
        cb = QApplication.clipboard()
        cb.clear()
        mimedata = QMimeData()
        urls = []

        s1 = slice(self.anchor.y(), self.anchor.y() + self.d)
        s2 = slice(self.anchor.x(), self.anchor.x() + self.d)
        height, width, depth = self.origin.shape
        for i in range(depth):
            img = np.zeros((self.d, self.d, depth))
            img[:, :, i] = self.origin[s1, s2, i]
            path = self.imwrite(f'{i}.png', img, width)
            urls.append(QUrl.fromLocalFile(path))
        if depth > 1:
            path = self.imwrite('fusion.png', self.origin[s1, s2], width)
            urls.append(QUrl.fromLocalFile(path))
        mimedata.setUrls(urls)
        cb.setMimeData(mimedata)
        self.printf(f'Src size{self.origin.shape}', f'RoI width: {self.d}')
