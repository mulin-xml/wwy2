from PySide6.QtWidgets import QApplication, QDialog, QGraphicsScene
from PySide6.QtGui import QTextCursor, QImage, QPixmap
from lib.ui import Ui_Dialog

import numpy as np
import sys


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.logger = self.ui.textEdit.textCursor()

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # 补充连线
        self.ui.pushButton_8.clicked.connect(self.ui.tab_17.openfile)
        self.ui.pushButton.clicked.connect(self.ui.tab_17.savefile)
        self.ui.pushButton_9.clicked.connect(self.ui.tab_18.openfile)

    def printf(self, *value):
        self.logger.movePosition(QTextCursor.MoveOperation.End)
        for i in value:
            self.logger.insertText(f'{i} ')
        self.logger.insertText('\n')

    def imshow(self, img: np.ndarray, form):
        height, width, depth = img.shape
        frame = QImage(img, width, height, width * depth * img.itemsize, form)
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(frame))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
