from PySide6.QtWidgets import QTabWidget
from PySide6.QtGui import QMouseEvent, QImage
from PySide6.QtCore import Signal, Slot, QPoint, QPointF


class MyTabWidget(QTabWidget):

    @Slot(int, QPointF)
    def on_mouse(self, type, pos: QPointF):
        self.currentWidget().on_mouse(type, pos.toPoint())
