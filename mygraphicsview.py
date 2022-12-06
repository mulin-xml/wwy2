from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QMouseEvent, QImage
from PySide6.QtCore import Signal


class MyGraphicsView(QGraphicsView):
    mouseSig = Signal(int, QMouseEvent)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mouseSig.emit(0, event)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mouseSig.emit(1, event)
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.mouseSig.emit(2, event)
        return super().mouseMoveEvent(event)
