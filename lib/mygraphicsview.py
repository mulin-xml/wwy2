from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QMouseEvent, QWheelEvent
from PySide6.QtCore import Signal, Qt, QPointF


class MyGraphicsView(QGraphicsView):
    mouseSig = Signal(int, QPointF)

    def __init__(self, parent):
        super(MyGraphicsView, self).__init__(parent)
        self.anchor = QPointF()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            self.anchor = event.position()
        elif event.buttons() == Qt.MouseButton.LeftButton:
            self.mouseSig.emit(0, self.mapToScene(event.pos()))
        else:
            pass
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.MouseButton.RightButton:
            delta = event.position() - self.anchor
            self.anchor = event.position()
            # 必须设置为TransformationAnchor::NoAnchor
            self.translate(delta.x() / self.transform().m11(), delta.y() / self.transform().m22())
        elif event.buttons() == Qt.MouseButton.LeftButton:
            self.mouseSig.emit(2, self.mapToScene(event.pos()))
        else:
            pass
        return super().mouseMoveEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        # 必须设置为ResizeAnchor::AnchorUnderMouse
        if event.angleDelta().y() > 0:
            self.scale(1.2, 1.2)
        else:
            self.scale(1 / 1.2, 1 / 1.2)
        return super().wheelEvent(event)
