# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circular_controler.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CircularControler(object):
    def setupUi(self, CircularControler):
        if not CircularControler.objectName():
            CircularControler.setObjectName(u"CircularControler")
        CircularControler.resize(274, 688)
        CircularControler.setStyleSheet(u"QFrame#circular_background{\n"
"	background-color: rgb(27, 28, 56);\n"
"	border-radius: 125px;\n"
"}\n"
"\n"
"QFrame#circular_main{\n"
"	background-color: rgb(50, 50, 88);\n"
"	border-radius: 105px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#down_button, #up_button{\n"
"	border-radius: 25px;\n"
"	border: 1px solid #1B1B38;\n"
"}\n"
"\n"
"QPushButton#down_button::pressed, #up_button::pressed{\n"
"	background-color: #B18AFF;\n"
"}\n"
"\n"
"QPushButton#power_button{\n"
"	border-radius: 35px;\n"
"	border: 1px solid #1B1B38;\n"
"}\n"
"\n"
"QPushButton#power_button::pressed{\n"
"	background-color: #B18AFF;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(CircularControler)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.circular_background = QFrame(CircularControler)
        self.circular_background.setObjectName(u"circular_background")
        self.circular_background.setMinimumSize(QSize(250, 250))
        self.circular_background.setMaximumSize(QSize(250, 250))
        self.circular_background.setStyleSheet(u"")
        self.circular_background.setFrameShape(QFrame.Shape.NoFrame)
        self.circular_background.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.circular_background)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.circular_prog = QFrame(self.circular_background)
        self.circular_prog.setObjectName(u"circular_prog")
        self.circular_prog.setStyleSheet(u"")
        self.circular_prog.setFrameShape(QFrame.Shape.NoFrame)
        self.circular_prog.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.circular_prog)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.circular_main = QFrame(self.circular_prog)
        self.circular_main.setObjectName(u"circular_main")
        self.circular_main.setFrameShape(QFrame.Shape.NoFrame)
        self.circular_main.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.circular_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.temperature_label = QLabel(self.circular_main)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setMaximumSize(QSize(16777215, 50))
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.temperature_label)

        self.celsius_label = QLabel(self.circular_main)
        self.celsius_label.setObjectName(u"celsius_label")
        self.celsius_label.setMaximumSize(QSize(16777215, 20))
        self.celsius_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.celsius_label)

        self.verticalSpacer_2 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.circular_main)


        self.horizontalLayout_14.addWidget(self.circular_prog)


        self.verticalLayout.addWidget(self.circular_background)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_3 = QFrame(CircularControler)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(250, 120))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.down_button = QPushButton(self.frame_3)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setMinimumSize(QSize(50, 50))
        self.down_button.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_13.addWidget(self.down_button)

        self.power_button = QPushButton(self.frame_3)
        self.power_button.setObjectName(u"power_button")
        self.power_button.setMinimumSize(QSize(70, 70))
        self.power_button.setMaximumSize(QSize(70, 70))
        self.power_button.setCheckable(False)
        self.power_button.setChecked(False)

        self.horizontalLayout_13.addWidget(self.power_button)

        self.up_button = QPushButton(self.frame_3)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setMinimumSize(QSize(50, 50))
        self.up_button.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_13.addWidget(self.up_button)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(CircularControler)

        QMetaObject.connectSlotsByName(CircularControler)
    # setupUi

    def retranslateUi(self, CircularControler):
        CircularControler.setWindowTitle(QCoreApplication.translate("CircularControler", u"Form", None))
        self.temperature_label.setText(QCoreApplication.translate("CircularControler", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700;\">0\u00b0</span></p></body></html>", None))
        self.celsius_label.setText(QCoreApplication.translate("CircularControler", u"Celsius", None))
        self.down_button.setText("")
        self.power_button.setText("")
        self.up_button.setText("")
    # retranslateUi

