from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Slot
from uic.hist import Ui_Dialog


class Hist(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

    @Slot()
    def update(self, img): ...
