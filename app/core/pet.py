import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from app.ui.window import WindowInitializer
from app.ui.tray import TrayIcon
from app.animation.manager import AnimationManager



class DesktopPet(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.init_state()
        self.init_ui()
        self.init_managers()

    def init_state(self):
        self.condition = 0
        self.talk_condition = 0
        self.is_dragging = False
        self.is_follow_mouse = False

    def init_ui(self):
        self.window_init = WindowInitializer(self)
        self.tray = TrayIcon(self)
    
    def init_managers(self):
        self.animation_manager = AnimationManager(self)
        # self.dialog_manager = DialogManager(self)
        # self.mouse_handler = MouseHandler(self)