from PySide6.QtWidgets import QApplication, QDialog, QTextEdit,QGraphicsScene
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QTextCursor,QMouseEvent, QImage,QPixmap
from ui import Ui_Dialog

import n1c3_roi
import cv2
import numpy as np
import sys

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.logger = self.ui.textEdit
        self.txt = ''

        self.scene = QGraphicsScene()  
        self.ui.graphicsView.setScene(self.scene)  

        # 连线
        self.ui.pushButton_8.clicked.connect(self.ui.tab_17.openfile)


    def printf(self, t):
        self.txt += '\n'
        self.txt += t
        self.logger.setText(self.txt)
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        self.logger.textCursor()

    def on_changed(self, int):
        a = self.ui.tabWidget.currentWidget().objectName()
        self.printf(f'changed {a}')

    def imshow(self, img):
        y, x = img.shape[:-1]
        frame = QImage(img, x, y, QImage.Format.Format_BGR888)
        self.scene.clear()  # 先清空上次的残留
        self.pix = QPixmap.fromImage(frame)
        self.scene.addPixmap(self.pix)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
