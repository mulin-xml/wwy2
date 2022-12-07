from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QMouseEvent, QWheelEvent
from PySide6.QtCore import Signal, Qt, QPoint, QPointF


class MyGraphicsView(QGraphicsView):
    mouseSig = Signal(int, QMouseEvent)

    def __init__(self, parent):
        super(MyGraphicsView, self).__init__(parent)
        self.anchor = QPoint()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            self.anchor = event.pos()
            a = self.mapToScene(self.anchor)
            self.scene().addEllipse(a.x(), a.y(), 2, 2)
        else:
            self.mouseSig.emit(0, event)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mouseSig.emit(1, event)
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.MouseButton.RightButton:
            delta = event.pos() - self.anchor
            # center = QPoint(self.width() * 0.5 - delta.x(), self.height() * 0.5 - delta.y())
            # self.centerOn(self.mapToScene(center))
            sr = self.scene().sceneRect()
            self.scene().setSceneRect(sr.x() - delta.x(), sr.y() - delta.y(), sr.width(), sr.height())
        else:
            self.mouseSig.emit(2, event)
        return super().mouseMoveEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.angleDelta().y() > 0:
            self.scale(1.2, 1.2)
        else:
            self.scale(1 / 1.2, 1 / 1.2)
        return super().wheelEvent(event)
