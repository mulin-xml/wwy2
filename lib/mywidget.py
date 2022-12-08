from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage
from PySide6.QtCore import QPoint
from lib.mygraphicsview import MyGraphicsView
from typing import cast


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form: QImage.Format

    def on_mouse(self, action: int, pos: QPoint): ...

    def init(self):
        self.gv = cast(MyGraphicsView, self.findChild(MyGraphicsView))
        self.gv.mouseSig.connect(self.on_mouse)

    def imshow(self, img):
        self.gv.imshow(img, self.form)

    def printf(self, *value):
        self.parent().parent().parent().printf(*value)
