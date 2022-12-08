from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot, QPoint
import numpy as np
import cv2
import sys


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.logger = self.parent().parent().parent().textEdit

    def on_mouse(self, action: int, pos: QPoint): ...

    def imshow(self, img, form):
        self.parent().parent().parent().imshow(img, form)

    def printf(self, *value):
        self.parent().parent().parent().printf(*value)
