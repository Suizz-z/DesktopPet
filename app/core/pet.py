import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from app.ui.window import WindowInitializer
from app.ui.tray import TrayIcon

class DesktopPet(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        
    def init_ui(self):
        self.window_init = WindowInitializer(self)
        self.tray = TrayIcon(self)