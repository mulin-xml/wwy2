from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QMouseEvent, QWheelEvent, QImage, QPixmap
from PySide6.QtCore import Signal, Qt, QPointF, QPoint
import numpy as np


class MyGraphicsView(QGraphicsView):
    mouseSig = Signal(int, QPoint)

    def __init__(self, parent):
        super(MyGraphicsView, self).__init__(parent)

        self.anchor = QPointF()
        self.sc = QGraphicsScene()
        self.setScene(self.sc)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.NoAnchor)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            self.anchor = event.position()
        elif event.buttons() == Qt.MouseButton.LeftButton:
            self.mouseSig.emit(0, self.mapToScene(event.pos()).toPoint())
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
            self.mouseSig.emit(1, self.mapToScene(event.pos()).toPoint())
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

    def imshow(self, img: np.ndarray, form):
        height, width, depth = img.shape
        frame = QImage(img, width, height, width * depth * img.itemsize, form)
        self.sc.clear()
        self.sc.addPixmap(QPixmap.fromImage(frame))
