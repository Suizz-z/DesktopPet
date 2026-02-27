from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from utils.OT.Ui_fanyi import Ui_Form
from utils.OT.tools import translate,bind_target_lang,change_target_lang
import requests

class FanYiWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.sourceLang = 'auto'
        self.targetLang = 'en-US'
        self.sourceText = ''
        self.setupUi(self)
        bind_target_lang(self.targetLangComboBox)
        self.autoRadioButton.clicked.connect(self.changeTargetLang)
        self.zhRadioButton.clicked.connect(self.changeTargetLang)
        self.enRadioButton.clicked.connect(self.changeTargetLang)
        self.translateButton.clicked.connect(self.buttonTranslate)
        self.setAttribute(Qt.WA_QuitOnClose, False)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def changeTargetLang(self):
        if self.autoRadioButton.isChecked():
            self.sourceLang = 'auto'
            print(self.sourceLang)
        elif self.zhRadioButton.isChecked():
            self.sourceLang = 'zh-CN'
            print(self.sourceLang)
        elif self.enRadioButton.isChecked():
            self.sourceLang = 'en-US'
            print(self.sourceLang)

    def buttonTranslate(self):
        self.targetLangplainTextEdit.setPlainText('')
        content = self.sourceLangplainTextEdit.toPlainText()
        target_lang = change_target_lang(self.targetLangComboBox.currentText())
        print(target_lang)
        sourceLang = self.sourceLang
        if content == '':
            self.logPlainTextEdit.setPlainText('请输入要翻译的内容')
            return
        result = translate(content,sourceLang,target_lang)
        print(result)
        self.targetLangplainTextEdit.setPlainText(result)
        self.logPlainTextEdit.setPlainText('翻译完成')
        

if __name__ == '__main__':
    app = QApplication([])
    window = FanYiWindow()
    window.show()
    app.exec()

    # window.translate('我是一个学生')
