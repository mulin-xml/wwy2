from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot
import numpy as np
import cv2
import sys


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.logger = self.parent().parent().parent().textEdit

    def on_mouse(self, type, event):
        pass

    def imshow(self, img):
        self.parent().parent().parent().imshow(img)

    def printf(self, t):
        self.parent().parent().parent().printf(t)
