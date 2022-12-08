from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QTextCursor
from lib.ui import Ui_Dialog
import sys


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.logger = self.ui.textEdit

        # 补充连线
        self.ui.tab_N1C3_RoI.init()
        self.ui.tab_NxC1_RoI.init()
        self.ui.pushButton_8.clicked.connect(self.ui.tab_N1C3_RoI.openfile)
        self.ui.pushButton.clicked.connect(self.ui.tab_N1C3_RoI.savefile)
        self.ui.pushButton_9.clicked.connect(self.ui.tab_NxC1_RoI.openfile)
        self.ui.pushButton_2.clicked.connect(self.ui.tab_NxC1_RoI.savefile)

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
