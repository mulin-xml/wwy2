from PySide6.QtWidgets import QTabWidget
from PySide6.QtGui import QMouseEvent, QImage
from PySide6.QtCore import Signal, Slot


class MyTabWidget(QTabWidget):

    @Slot(int, QMouseEvent)
    def on_mouse(self, type, event):
        self.currentWidget().on_mouse(type, event)
