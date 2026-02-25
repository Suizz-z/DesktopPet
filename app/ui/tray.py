import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class TrayIcon:
    def __init__(self, pet):
        self.pet = pet
        self.tray_icon_path = os.path.join('resources','icon.png')
        self.init_tray()

    def init_tray(self):
        quit_action = QAction('退出', self.pet, triggered=self.quit)
        quit_action.setIcon(QIcon(self.tray_icon_path))
        showing = QAction(u'显示', self.pet, triggered=self.showwin)
        self.tray_icon_menu = QMenu(self.pet)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon_menu.addAction(showing)
        self.tray_icon = QSystemTrayIcon(self.pet)
        self.tray_icon.setIcon(QIcon(self.tray_icon_path))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

    def quit(self):
        self.pet.close()
        sys.exit()
 
    def showwin(self):
        self.pet.setWindowOpacity(1)
