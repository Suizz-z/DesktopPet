from PySide6.QtWidgets import *
import sys
from app.core.pet import DesktopPet

def main():
    app = QApplication([])
    pet = DesktopPet()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()