from PySide6.QtWidgets import QTabWidget
from PySide6.QtCore import Slot, QPoint
from lib.functions import *


class MyTabWidget(QTabWidget):
    def init_async(self):
        ui = self.parent()
        self.functions = [RoI(ui),
                          CircleCounter(ui), ]

    @property
    def func(self) -> BaseFunction:
        return self.functions[self.currentIndex()]

    @Slot(int, QPoint)
    def on_mouse(self, action: int, pos: QPoint):
        self.func.on_mouse(action, pos)

    def render_img(self):
        self.func.render_img()
