from PySide6.QtWidgets import QApplication, QDialog, QTextEdit
from PySide6.QtGui import QTextCursor
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
        self.ui.tab_17.parent().parent().parent().p()
    def p(self):
        print('got')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    # print(window.ui.tab_17.aaa)

    sys.exit(app.exec())
