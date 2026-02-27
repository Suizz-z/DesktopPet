# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

from qfluentwidgets import ImageLabel

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(751, 514)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.history = QPushButton(Form)
        self.history.setObjectName(u"history")

        self.gridLayout_2.addWidget(self.history, 9, 0, 1, 3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(55, 30))
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 7, 0, 1, 3)

        self.createWorld = QTextEdit(Form)
        self.createWorld.setObjectName(u"createWorld")
        self.createWorld.setMaximumSize(QSize(250, 50))
        font1 = QFont()
        font1.setPointSize(8)
        self.createWorld.setFont(font1)

        self.gridLayout_2.addWidget(self.createWorld, 1, 0, 1, 1)

        self.createName = QTextEdit(Form)
        self.createName.setObjectName(u"createName")
        self.createName.setMaximumSize(QSize(200, 50))
        self.createName.setFont(font1)

        self.gridLayout_2.addWidget(self.createName, 1, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.eegenerate = QPushButton(Form)
        self.eegenerate.setObjectName(u"eegenerate")

        self.gridLayout_2.addWidget(self.eegenerate, 8, 0, 1, 3)

        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(55, 30))

        self.gridLayout_2.addWidget(self.image, 3, 2, 1, 1)

        self.roleImage = ImageLabel(Form)
        self.roleImage.setObjectName(u"roleImage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roleImage.sizePolicy().hasHeightForWidth())
        self.roleImage.setSizePolicy(sizePolicy)
        self.roleImage.setMinimumSize(QSize(0, 0))
        self.roleImage.setMaximumSize(QSize(200, 250))

        self.gridLayout_2.addWidget(self.roleImage, 6, 2, 1, 1)

        self.startCreate = QPushButton(Form)
        self.startCreate.setObjectName(u"startCreate")

        self.gridLayout_2.addWidget(self.startCreate, 1, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.textWorld = QPlainTextEdit(Form)
        self.textWorld.setObjectName(u"textWorld")
        self.textWorld.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.textWorld, 6, 0, 1, 1)

        self.textRole = QTextEdit(Form)
        self.textRole.setObjectName(u"textRole")
        self.textRole.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.textRole, 6, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(55, 30))

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4eba\u8bbe\u7ba1\u7406", None))
        self.history.setText(QCoreApplication.translate("Form", u"\u5386\u53f2\u8bb0\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e16\u754c\u89c2", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u8bbe\u5b9a", None))
        self.createWorld.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u4e16\u754c\u89c2\u4e3b\u9898(\u5982\uff1a\u6b66\u4fa0\u4e16\u754c\u3001\u9b54\u6cd5\u4e16\u754c\u7b49)", None))
        self.createName.setPlaceholderText(QCoreApplication.translate("Form", u"\u684c\u5ba0\u540d\u79f0(\u82e5\u4e3a\u7a7a\u5219\u968f\u673a\u751f\u6210)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
        self.eegenerate.setText(QCoreApplication.translate("Form", u"\u91cd\u65b0\u751f\u6210", None))
        self.image.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.roleImage.setText(QCoreApplication.translate("Form", u"\u6682\u65e0", None))
        self.startCreate.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u751f\u6210", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4eba\u8bbe\u751f\u6210", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u8bbe\u5b9a", None))
    # retranslateUi

