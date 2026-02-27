# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanyi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(630, 443)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 10, 610, 424))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sourceLangplainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.sourceLangplainTextEdit.setObjectName(u"sourceLangplainTextEdit")
        self.sourceLangplainTextEdit.setMaximumSize(QSize(16777215, 150))

        self.gridLayout.addWidget(self.sourceLangplainTextEdit, 2, 0, 1, 1)

        self.targetLangplainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.targetLangplainTextEdit.setObjectName(u"targetLangplainTextEdit")
        self.targetLangplainTextEdit.setEnabled(True)
        self.targetLangplainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.targetLangplainTextEdit, 1, 1, 3, 1)

        self.translateButton = QPushButton(self.layoutWidget)
        self.translateButton.setObjectName(u"translateButton")

        self.gridLayout.addWidget(self.translateButton, 3, 0, 1, 1)

        self.logPlainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")
        self.logPlainTextEdit.setEnabled(False)

        self.gridLayout.addWidget(self.logPlainTextEdit, 4, 0, 1, 2)

        self.targetLangComboBox = QComboBox(self.layoutWidget)
        self.targetLangComboBox.setObjectName(u"targetLangComboBox")

        self.gridLayout.addWidget(self.targetLangComboBox, 0, 1, 1, 1)

        self.sourceLangGroupBox = QGroupBox(self.layoutWidget)
        self.sourceLangGroupBox.setObjectName(u"sourceLangGroupBox")
        self.horizontalLayout = QHBoxLayout(self.sourceLangGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.autoRadioButton = QRadioButton(self.sourceLangGroupBox)
        self.autoRadioButton.setObjectName(u"autoRadioButton")

        self.horizontalLayout.addWidget(self.autoRadioButton)

        self.zhRadioButton = QRadioButton(self.sourceLangGroupBox)
        self.zhRadioButton.setObjectName(u"zhRadioButton")

        self.horizontalLayout.addWidget(self.zhRadioButton)

        self.enRadioButton = QRadioButton(self.sourceLangGroupBox)
        self.enRadioButton.setObjectName(u"enRadioButton")

        self.horizontalLayout.addWidget(self.enRadioButton)


        self.gridLayout.addWidget(self.sourceLangGroupBox, 0, 0, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5728\u7ebf\u7ffb\u8bd1", None))
        self.translateButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u7ffb\u8bd1", None))
        self.targetLangComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8f93\u51fa\u7684\u8bed\u8a00", None))
        self.sourceLangGroupBox.setTitle(QCoreApplication.translate("Form", u"\u9009\u62e9\u8f93\u5165\u7684\u8bed\u8a00", None))
        self.autoRadioButton.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u68c0\u6d4b", None))
        self.zhRadioButton.setText(QCoreApplication.translate("Form", u"\u4e2d\u6587", None))
        self.enRadioButton.setText(QCoreApplication.translate("Form", u"\u82f1\u6587", None))
    # retranslateUi

