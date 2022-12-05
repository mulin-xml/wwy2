from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot
import skimage.io
import cv2
import sys


class Cfg:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Cfg, cls).__new__(cls)
        return cls._instance
    origins = None
    origin = None
    xx, yy = 0, 0
    d = 0


class Printf():
    def __init__(self, widget: QTextEdit) -> None:
        self.txt = ''
        self.widget = widget

    def __call__(self, t) -> None:
        self.txt += '\n'
        self.txt += t
        self.widget.setText(self.txt)
        self.widget.moveCursor(QTextCursor.MoveOperation.End)


def on_mouse(event, x, y, flags: int, cfg: Cfg):
    if event == cv2.EVENT_LBUTTONDOWN:
        cfg.xx, cfg.yy = x, y
        printf(f'Anchor, ({cfg.xx}, {cfg.yy})')
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cfg.d = max(y - cfg.yy, x - cfg.xx)
        draw()


def on_pos(x):  # 作为回调函数输出当前滑动条的位置
    cfg = Cfg()
    img = cfg.origins[x]
    cv2.normalize(img, img, 0, 65535, cv2.NORM_MINMAX)
    cfg.origin = cv2.resize(img, (0, 0), img, 0.5, 0.5)
    draw()


def draw():
    cfg = Cfg()
    img = cfg.origin.copy()
    cv2.rectangle(img, (cfg.xx, cfg.yy), (cfg.xx + cfg.d, cfg.yy + cfg.d), (0, 255, 0), 2)
    cv2.imshow('image', img)


@Slot()
def button_clicked():
    path, _ = QFileDialog().getOpenFileName()
    printf(path)
    cfg = Cfg()
    cfg.origins = skimage.io.imread(path)
    print(cfg.origins.shape)
    cv2.namedWindow('image')
    on_pos(0)
    cv2.setMouseCallback('image', on_mouse, cfg)
    cv2.createTrackbar('r', 'image', 0, cfg.origins.shape[0] - 1, on_pos)
    cnt = 0
    while (k := cv2.waitKey(1)) != ord('q'):
        if k == ord('p'):
            cv2.imwrite(f'{cnt}.jpg', cfg.origin[cfg.yy:cfg.yy + cfg.d, cfg.xx:cfg.xx + cfg.d] / 256)
            cnt += 1
            printf(f'{cfg.d}, {cfg.origin.shape}')
    cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    button = QPushButton("打开图片")
    button.clicked.connect(button_clicked)
    label = QTextEdit()
    label.setReadOnly(True)
    printf = Printf(label)

    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(label)
    window = QWidget()
    window.setLayout(layout)
    # window.setBaseSize(500, 500)
    window.show()
    app.exec()
