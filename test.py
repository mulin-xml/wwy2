from skimage import io
import cv2
import numpy as np

# path = '\\\\192.168.1.200\\share\\10 60X16HD2_Brightfield.stk'

# a = io.imread(path)
# img = a[0]
# cv2.normalize(img, img, 0, 65535, cv2.NORM_MINMAX)
# cv2.imshow('1', img)
# cv2.waitKey()

import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

def j():
    print('j')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "untitled.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)

    window.pushButton_8.clicked.connect(j)
    window.show()
    sys.exit(app.exec())
