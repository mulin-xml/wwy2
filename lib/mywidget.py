from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage
from PySide6.QtCore import QPoint
from lib.mygraphicsview import MyGraphicsView
from typing import cast
import numpy as np
import cv2

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from lib.ui import Ui_Dialog


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form: QImage.Format
        self.ui: Ui_Dialog

    def on_mouse(self, action: int, pos: QPoint): ...

    def init(self, ui):
        self.ui = ui
        self.gv = cast(MyGraphicsView, self.findChild(MyGraphicsView))
        self.gv.mouseSig.connect(self.on_mouse)

    def imshow(self, img):
        self.gv.imshow(img, self.form)

    def printf(self, *value):
        self.parent().parent().parent().printf(*value)

    def imwrite(self, name: str, img: np.ndarray):
        if self.ui.line_check.isChecked():
            cv2.line(img, (img.shape[1] - 20, img.shape[0] - 20), (img.shape[1] - 80, img.shape[0] - 20), [255] * 3, 3)
        cv2.imwrite(name, img)
