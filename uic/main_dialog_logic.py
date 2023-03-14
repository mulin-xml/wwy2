from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt
from uic.main_dialog import Ui_Dialog


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, True)
        self.tab1.setupUi(self)

    def printf(self, *value):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        cursor = self.logger.textCursor()
        for i in value:
            cursor.insertText(f'{i} ')
        cursor.insertText('\n')
