from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt, Slot
from lib.ui import Ui_Dialog
from PIL import Image
import numpy as np
import tifffile
import cv2
import sys


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, True)
        self.imgSlider.setEnabled(False)
        self.controlTabWidget.init_async()

        self.img: np.ndarray = None
        self.stk: np.ndarray = None

        # 手动信号槽
        self.gv.mouseSig.connect(self.controlTabWidget.on_mouse)

    @Slot(int)
    def on_imgSlider_valueChanged(self, value):
        self.img = self.stk[value]
        self.img_preprocess()
        self.controlTabWidget.render_img()

    @Slot(int)
    def on_controlTabWidget_currentChanged(self, index):
        if self.img is not None:
            self.controlTabWidget.render_img()

    @Slot()
    def on_openImgButton_clicked(self):
        path, _ = QFileDialog().getOpenFileName()
        if not path:
            self.printf('User presses cancel.')
            return
        path: str
        if path.endswith('.stk'):
            self.imgSlider.setEnabled(True)
            self.stk = tifffile.imread(path)
            self.imgSlider.setRange(0, self.stk.shape[0] - 1)
            self.img = self.stk[0]
        else:
            self.imgSlider.setEnabled(False)
            self.img = np.array(Image.open(path))
        self.imgSlider.setValue(0)
        self.img_preprocess()

    def img_preprocess(self):
        if self.img.itemsize == 2:
            self.img = cv2.normalize(self.img, None, 0, 255, cv2.NORM_MINMAX)
            self.img = self.img.astype(np.uint8)
        if self.img.ndim == 2:
            self.img = self.img[:, :, None]
        elif self.img.ndim == 3:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        else:
            self.printf(f'Error: img.shape is {self.img.shape}.')
        self.gv.imshow(self.img)

    def printf(self, *value):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        cursor = self.logger.textCursor()
        for i in value:
            cursor.insertText(f'{i} ')
        cursor.insertText('\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
