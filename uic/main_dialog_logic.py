from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt
from uic.hist_logic import Hist
from uic.main_dialog import Ui_Dialog


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, True)

        self.hist = Hist()
        self.tab1.setupUi(self)

    def closeEvent(self, arg__1) -> None:
        self.hist.close()
        return super().closeEvent(arg__1)

    def on_openHistButton_clicked(self):
        self.hist.show()
        self.printf('User open hist.')

    def printf(self, *value):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        cursor = self.logger.textCursor()
        for i in value:
            cursor.insertText(f'{i} ')
        cursor.insertText('\n')
