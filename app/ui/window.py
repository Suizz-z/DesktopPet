from PySide6.QtCore import *

class WindowInitializer:
    def __init__(self, pet):
        self.pet = pet
        self.init_window()
    
    def init_window(self):
        self.pet.setWindowFlags(
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint | 
            Qt.SubWindow
        )
        self.pet.setAutoFillBackground(False)
        self.pet.setAttribute(Qt.WA_TranslucentBackground, True)