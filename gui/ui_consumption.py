# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consumption.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Consumption(object):
    def setupUi(self, Consumption):
        if not Consumption.objectName():
            Consumption.setObjectName(u"Consumption")
        Consumption.resize(376, 305)
        self.horizontalLayout = QHBoxLayout(Consumption)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.circular_cc_bg = QFrame(Consumption)
        self.circular_cc_bg.setObjectName(u"circular_cc_bg")
        self.circular_cc_bg.setMinimumSize(QSize(120, 120))
        self.circular_cc_bg.setMaximumSize(QSize(120, 120))
        self.circular_cc_bg.setFrameShape(QFrame.Shape.NoFrame)
        self.circular_cc_bg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.circular_cc_bg)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.circular_cc_prog = QFrame(self.circular_cc_bg)
        self.circular_cc_prog.setObjectName(u"circular_cc_prog")
        self.circular_cc_prog.setStyleSheet(u"QFrame#circular_cc_prog{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(127, 169, 251, 0), stop:0.75 rgba(155, 0, 255, 255));\n"
"	border-radius: 60px;\n"
"}")
        self.circular_cc_prog.setFrameShape(QFrame.Shape.NoFrame)
        self.circular_cc_prog.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.circular_cc_prog)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.circular_cc_main = QFrame(self.circular_cc_prog)
        self.circular_cc_main.setObjectName(u"circular_cc_main")
        self.circular_cc_main.setFrameShape(QFrame.Shape.NoFrame)
        self.circular_cc_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.circular_cc_main)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label = QLabel(self.circular_cc_main)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label)


        self.horizontalLayout_22.addWidget(self.circular_cc_main)


        self.horizontalLayout_21.addWidget(self.circular_cc_prog)


        self.horizontalLayout.addWidget(self.circular_cc_bg)

        self.frame_12 = QFrame(Consumption)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.kwh_consumption_label = QLabel(self.frame_12)
        self.kwh_consumption_label.setObjectName(u"kwh_consumption_label")
        self.kwh_consumption_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.kwh_consumption_label)

        self.kwh_max_label = QLabel(self.frame_12)
        self.kwh_max_label.setObjectName(u"kwh_max_label")
        self.kwh_max_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.kwh_max_label)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)


        self.horizontalLayout.addWidget(self.frame_12)


        self.retranslateUi(Consumption)

        QMetaObject.connectSlotsByName(Consumption)
    # setupUi

    def retranslateUi(self, Consumption):
        Consumption.setWindowTitle(QCoreApplication.translate("Consumption", u"Form", None))
        self.label.setText(QCoreApplication.translate("Consumption", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">42%</span></p></body></html>", None))
        self.kwh_consumption_label.setText(QCoreApplication.translate("Consumption", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">6.421 kWh</span></p></body></html>", None))
        self.kwh_max_label.setText(QCoreApplication.translate("Consumption", u"<html><head/><body><p><span style=\"font-size:13px; font-weight:600; color:#b4b4db;\">out of 8.421 kWh</span></p></body></html>", None))
    # retranslateUi

