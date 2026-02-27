from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from Ui_cm import Ui_Form
import sys

import requests

class CharacterManagement(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cm = CharacterManagement()
    cm.show()
    sys.exit(app.exec())
