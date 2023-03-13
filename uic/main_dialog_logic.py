from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt, Slot
from uic.hist_logic import Hist
from uic.main_dialog import Ui_Dialog
from PIL import Image
import numpy as np
import tifffile
import cv2
from lib.functions import RoI


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, True)
        self.tab1ImgSlider.setEnabled(False)

        self.hist = Hist()
        self.fun1 = RoI(self)
        self.fun1.setupUi(self)

        # 手动信号槽
        # self.tab1GV.mouseSig.connect(self.fun1.on_mouse)

    def closeEvent(self, arg__1) -> None:
        self.hist.close()
        return super().closeEvent(arg__1)

    @Slot(int)
    def on_imgSlider_valueChanged(self, value):
        self.img = self.stk[value]
        self.img_preprocess()
        self.controlTabWidget.render_img()

    def on_openHistButton_clicked(self):
        self.hist.show()
        self.printf('User open hist.')

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
        '''
        目标图像切换时的预处理
        '''
        if self.img.itemsize == 2:
            # 16位图像转8位
            self.img = cv2.normalize(self.img, None, 0, 255, cv2.NORM_MINMAX)
            self.img = self.img.astype(np.uint8)

        if self.img.ndim == 2:  # 单通道图像
            self.img = self.img[:, :, None]
        elif self.img.ndim == 3:  # 3通道图像
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        else:
            self.printf(f'Error: img.shape is {self.img.shape}.')
        self.gv.imshow(self.img)
        self.hist.update(self.img)

    def printf(self, *value):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        cursor = self.logger.textCursor()
        for i in value:
            cursor.insertText(f'{i} ')
        cursor.insertText('\n')
