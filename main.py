from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QTextCursor
from lib.ui import Ui_Dialog

import sys


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.logger = self.ui.textEdit.textCursor()

        # 补充连线
        self.ui.tab_N1C3_RoI.init()
        self.ui.tab_NxC1_RoI.init()
        self.ui.pushButton_8.clicked.connect(self.ui.tab_N1C3_RoI.openfile)
        self.ui.pushButton.clicked.connect(self.ui.tab_N1C3_RoI.savefile)
        self.ui.pushButton_9.clicked.connect(self.ui.tab_NxC1_RoI.openfile)

    def printf(self, *value):
        self.logger.movePosition(QTextCursor.MoveOperation.End)
        for i in value:
            self.logger.insertText(f'{i} ')
        self.logger.insertText('\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
