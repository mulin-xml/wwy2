from PySide6.QtWidgets import QApplication, QDialog, QGraphicsScene
from PySide6.QtGui import QTextCursor, QImage, QPixmap, QColor
from PySide6.QtCore import Qt
from lib.ui import Ui_Dialog

import numpy as np
import sys
import cv2


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.logger = self.ui.textEdit
        self.txt = ''

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # 补充连线
        self.ui.pushButton_8.clicked.connect(self.ui.tab_17.openfile)
        self.ui.pushButton.clicked.connect(self.ui.tab_17.savefile)
        self.ui.pushButton_9.clicked.connect(self.ui.tab_18.openfile)

    def printf(self, t):
        self.txt += '\n'
        self.txt += t
        self.logger.setText(self.txt)
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        self.logger.textCursor()

    def imshow(self, img: np.ndarray):
        height, width, depth = img.shape
        frame = QImage(img, width, height, width * depth, self.__calc_format(depth))
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(frame))

    def __calc_format(self, depth):
        if depth == 1:
            return QImage.Format.Format_Grayscale8
        elif depth == 3:
            return QImage.Format.Format_BGR888
        elif depth == 4:
            return QImage.Format.Format_RGBA8888


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
