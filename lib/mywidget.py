from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage
from PySide6.QtCore import QPoint
from lib.mygraphicsview import MyGraphicsView
from typing import cast, TYPE_CHECKING

import numpy as np
import cv2
import os

if TYPE_CHECKING:
    from lib.ui import Ui_Dialog


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form: QImage.Format
        self.ui: Ui_Dialog

    def on_mouse(self, action: int, pos: QPoint): ...

    def init(self, ui):
        self.ui: Ui_Dialog = ui
        self.gv = cast(MyGraphicsView, self.findChild(MyGraphicsView))
        self.gv.mouseSig.connect(self.on_mouse)

    def imshow(self, img):
        self.gv.imshow(img, self.form)

    def printf(self, *value):
        self.parent().parent().parent().printf(*value)

    def imwrite(self, name: str, img: np.ndarray, origin_width=None) -> str:
        width = img.shape[1]
        if origin_width is None:
            origin_width = width
        rate = 1000 / width
        dst = cv2.resize(img, None, fx=rate, fy=rate)  # 宽度对齐1000px
        dst_width, dst_height = dst.shape[1], dst.shape[0]

        if self.ui.line_check.isChecked():
            margin = 100
            length = int(origin_width / float(self.ui.from_edit.text()) * float(self.ui.to_edit.text()) * rate)
            cv2.line(dst, (dst_width - margin - length, dst_height - margin), (dst_width - margin, dst_height - margin), [255] * 3, 4)
            cv2.putText(dst, f'{self.ui.to_edit.text()}um', (dst_width - margin - length, int(dst_height - margin * 1.3)), cv2.FONT_HERSHEY_DUPLEX, 1.5, [255] * 3, 2, cv2.LINE_AA)
        cv2.imwrite(name, dst)
        return os.path.join(os.getcwd(), name)
