from PySide6.QtWidgets import QTabWidget
from PySide6.QtCore import Slot, QPoint
from lib.functions import *


class MyTabWidget(QTabWidget):


    def render_img(self):
        self.func.render_img()
