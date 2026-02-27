from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import *
# from utils.CM.Ui_cm import Ui_Form
from Ui_cm import Ui_Form
import sys
import os

import requests

class CharacterManagement(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 使用绝对路径加载图片
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "role.png")
        self.roleImage.setImage(image_path)
        self.roleImage.scaledToHeight(200)
        self.roleImage.scaledToWidth(200)
        self.setAttribute(Qt.WA_QuitOnClose, False)

    def closeEvent(self, event):
        event.ignore()
        self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    cm = CharacterManagement()
    cm.show()
    sys.exit(app.exec())
