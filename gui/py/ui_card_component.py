# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_componentatkqvP.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_CardComponent(object):
    def setupUi(self, CardComponent):
        if not CardComponent.objectName():
            CardComponent.setObjectName(u"CardComponent")
        CardComponent.resize(705, 193)
        CardComponent.setStyleSheet(u"QFrame#frame{\n"
"	background-color: #323258;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#card_text{\n"
"	font-size: 18pt;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#card_button{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 #B18AFF, stop:1 #A16FFF);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#card_button::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 #D3BCFF, stop:1 #B18AFE);\n"
"}")
        self.horizontalLayout = QHBoxLayout(CardComponent)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CardComponent)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#card_frame_svg{\n"
"	background-color: #A16EFF;\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.card_frame_svg = QFrame(self.frame)
        self.card_frame_svg.setObjectName(u"card_frame_svg")
        self.card_frame_svg.setMinimumSize(QSize(91, 74))
        self.card_frame_svg.setMaximumSize(QSize(91, 74))
        self.card_frame_svg.setFrameShape(QFrame.StyledPanel)
        self.card_frame_svg.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.card_frame_svg)

        self.card_text = QLabel(self.frame)
        self.card_text.setObjectName(u"card_text")

        self.horizontalLayout_2.addWidget(self.card_text)

        self.card_button = QPushButton(self.frame)
        self.card_button.setObjectName(u"card_button")
        self.card_button.setMinimumSize(QSize(140, 48))
        self.card_button.setMaximumSize(QSize(140, 48))

        self.horizontalLayout_2.addWidget(self.card_button)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(CardComponent)

        QMetaObject.connectSlotsByName(CardComponent)
    # setupUi

    def retranslateUi(self, CardComponent):
        CardComponent.setWindowTitle(QCoreApplication.translate("CardComponent", u"Form", None))
        self.card_text.setText("")
        self.card_button.setText("")
    # retranslateUi

