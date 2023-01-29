from PySide6.QtWidgets import QApplication
from uic.main_dialog_logic import MainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
