# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmTcYWF.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1390, 657)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1710, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel, QPushButton{\n"
"	color: white;\n"
"}\n"
"\n"
"QWidget#top_menu_frame{\n"
"	background-color: #323258;\n"
"}\n"
"\n"
"Line{\n"
"	background-color: #1B1B38;\n"
"	max-height: 20px;\n"
"}\n"
"\n"
"QLabel#user_name{\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel#system_name{\n"
"	color: #FFFFFF;\n"
"	font: \"Noto Sans\";\n"
"	font-size: 28px;\n"
"}\n"
"\n"
"QFrame#right_menu{\n"
"	background-color: #323258;\n"
"}\n"
"\n"
"QFrame#left_main{\n"
"	background-color: #1B1C38;\n"
"}\n"
"\n"
"QPushButton#hamburger_menu{\n"
"	background-image: url(:/icons/resources/icons/menu-outline.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#search_button{\n"
"	background-image: url(:/icons/resources/icons/search-outline.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#temperature_button, #humidity_button{\n"
"	font-weight:bold;\n"
"	border:"
                        " none;\n"
"	color: #AFAFD6;\n"
"	min-height: 35px;\n"
"}\n"
"\n"
"QPushButton#temperature_button::hover, #humidity_button::hover{\n"
"	color: #B18AFF;\n"
"	border-bottom: 4px solid #B18AFF;\n"
"}\n"
"\n"
"QPushButton#temperature_button::checked, #humidity_button::checked{\n"
"	color: #9165E7;\n"
"	border-bottom: 4px solid #9165E7;\n"
"}\n"
"\n"
"QFrame#frame_controls, #frame_consumption, #frame_traffic{\n"
"	background-color: #323258;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
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
"\n"
"\n"
"\n"
"QFrame#circular_background{\n"
"	background-color: rgb(27, 28, 56);\n"
"	border-radius: 125px;\n"
"}\n"
"\n"
"QFr"
                        "ame#circular_main{\n"
"	background-color: rgb(50, 50, 88);\n"
"	border-radius: 105px;\n"
"}\n"
"\n"
"QFrame#frame_chart{\n"
"	background-color: #323258;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#eletricity_button, #devices_button{\n"
"	font-weight:bold;\n"
"	border: none;\n"
"	color: #AFAFD6;\n"
"	min-height: 35px;\n"
"}\n"
"\n"
"QPushButton#eletricity_button::hover, #devices_button::hover{\n"
"	color: #B18AFF;\n"
"	border-bottom: 4px solid #B18AFF;\n"
"}\n"
"\n"
"QPushButton#eletricity_button::checked, #devices_button::checked{\n"
"	color: #9165E7;\n"
"	border-bottom: 4px solid #9165E7;\n"
"}\n"
"\n"
"QFrame#main_frame_consumption, #main_frame_traffic{\n"
"	border-top: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel#label_consumption, #label_traffic{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QFrame#circular_cc_bg{\n"
"	background-color: rgb(27, 28, 56);\n"
"	border-radius: 60px;\n"
"}\n"
"\n"
"QFrame#circular_cc_main{\n"
"	background-color: rgb(50, 50, 88);\n"
"	border-radiu"
                        "s: 48px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_menu_frame = QFrame(self.centralwidget)
        self.top_menu_frame.setObjectName(u"top_menu_frame")
        self.top_menu_frame.setMinimumSize(QSize(0, 76))
        self.top_menu_frame.setMaximumSize(QSize(16777215, 76))
        self.top_menu_frame.setFrameShape(QFrame.NoFrame)
        self.top_menu_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.top_menu_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.top_menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hamburger_menu = QPushButton(self.frame)
        self.hamburger_menu.setObjectName(u"hamburger_menu")
        self.hamburger_menu.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.hamburger_menu)


        self.horizontalLayout.addWidget(self.frame)

        self.line = QFrame(self.top_menu_frame)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(1, 22))
        self.line.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(self.top_menu_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.system_name = QLabel(self.frame_2)
        self.system_name.setObjectName(u"system_name")

        self.horizontalLayout_7.addWidget(self.system_name)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.top_menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(62, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.search_button = QPushButton(self.frame_5)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMaximumSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.search_button)


        self.horizontalLayout.addWidget(self.frame_5)

        self.line_2 = QFrame(self.top_menu_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(1, 22))
        self.line_2.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.frame_6 = QFrame(self.top_menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(62, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.email_icon = QLabel(self.frame_6)
        self.email_icon.setObjectName(u"email_icon")
        self.email_icon.setPixmap(QPixmap(u":/icons/resources/icons/email-outline.svg"))
        self.email_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.email_icon)


        self.horizontalLayout.addWidget(self.frame_6)

        self.line_3 = QFrame(self.top_menu_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(1, 22))
        self.line_3.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.frame_7 = QFrame(self.top_menu_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(62, 16777215))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.notification_icon = QLabel(self.frame_7)
        self.notification_icon.setObjectName(u"notification_icon")
        self.notification_icon.setPixmap(QPixmap(u":/icons/resources/icons/bell-outline.svg"))
        self.notification_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.notification_icon)


        self.horizontalLayout.addWidget(self.frame_7)

        self.line_4 = QFrame(self.top_menu_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(1, 22))
        self.line_4.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.frame_8 = QFrame(self.top_menu_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(170, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.user_pic = QLabel(self.frame_8)
        self.user_pic.setObjectName(u"user_pic")
        self.user_pic.setMaximumSize(QSize(50, 50))
        self.user_pic.setPixmap(QPixmap(u":/images/resources/images/86445195.png"))
        self.user_pic.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.user_pic)

        self.user_name = QLabel(self.frame_8)
        self.user_name.setObjectName(u"user_name")

        self.horizontalLayout_6.addWidget(self.user_name)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.top_menu_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.right_menu = QFrame(self.main_frame)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(251, 0))
        self.right_menu.setMaximumSize(QSize(251, 16777215))
        self.right_menu.setStyleSheet(u"")
        self.right_menu.setFrameShape(QFrame.NoFrame)
        self.right_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.right_menu)

        self.left_main = QFrame(self.main_frame)
        self.left_main.setObjectName(u"left_main")
        self.left_main.setFrameShape(QFrame.NoFrame)
        self.left_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_main)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(36, 36, 36, 36)
        self.top_main_frame = QFrame(self.left_main)
        self.top_main_frame.setObjectName(u"top_main_frame")
        self.top_main_frame.setMaximumSize(QSize(16777215, 96))
        self.top_main_frame.setFrameShape(QFrame.NoFrame)
        self.top_main_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.top_main_frame)

        self.middle_main_frame = QFrame(self.left_main)
        self.middle_main_frame.setObjectName(u"middle_main_frame")
        self.middle_main_frame.setMaximumSize(QSize(16777215, 96))
        self.middle_main_frame.setFrameShape(QFrame.NoFrame)
        self.middle_main_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.middle_main_frame)

        self.frame_9 = QFrame(self.left_main)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_controls = QFrame(self.frame_9)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setMaximumSize(QSize(320, 16777215))
        self.frame_controls.setFrameShape(QFrame.NoFrame)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_controls)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 0, 12, 12)
        self.frame_10 = QFrame(self.frame_controls)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 55))
        self.frame_10.setMaximumSize(QSize(16777215, 55))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.temperature_button = QPushButton(self.frame_10)
        self.temperature_button.setObjectName(u"temperature_button")
        self.temperature_button.setCheckable(True)
        self.temperature_button.setChecked(True)

        self.horizontalLayout_10.addWidget(self.temperature_button)

        self.humidity_button = QPushButton(self.frame_10)
        self.humidity_button.setObjectName(u"humidity_button")
        self.humidity_button.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.humidity_button)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.stackedWidget = QStackedWidget(self.frame_controls)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.temperature = QWidget()
        self.temperature.setObjectName(u"temperature")
        self.horizontalLayout_12 = QHBoxLayout(self.temperature)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(12, -1, -1, -1)
        self.circular_background = QFrame(self.temperature)
        self.circular_background.setObjectName(u"circular_background")
        self.circular_background.setMinimumSize(QSize(250, 250))
        self.circular_background.setMaximumSize(QSize(250, 250))
        self.circular_background.setStyleSheet(u"")
        self.circular_background.setFrameShape(QFrame.NoFrame)
        self.circular_background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.circular_background)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.circular_prog = QFrame(self.circular_background)
        self.circular_prog.setObjectName(u"circular_prog")
        self.circular_prog.setStyleSheet(u"")
        self.circular_prog.setFrameShape(QFrame.NoFrame)
        self.circular_prog.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.circular_prog)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.circular_main = QFrame(self.circular_prog)
        self.circular_main.setObjectName(u"circular_main")
        self.circular_main.setFrameShape(QFrame.NoFrame)
        self.circular_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.circular_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.temperature_label = QLabel(self.circular_main)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setMaximumSize(QSize(16777215, 40))
        self.temperature_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.temperature_label)

        self.celsius_label = QLabel(self.circular_main)
        self.celsius_label.setObjectName(u"celsius_label")
        self.celsius_label.setMaximumSize(QSize(16777215, 10))
        self.celsius_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.celsius_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.circular_main)


        self.horizontalLayout_14.addWidget(self.circular_prog)


        self.horizontalLayout_12.addWidget(self.circular_background)

        self.stackedWidget.addWidget(self.temperature)
        self.humidity = QWidget()
        self.humidity.setObjectName(u"humidity")
        self.horizontalLayout_11 = QHBoxLayout(self.humidity)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.humidity)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.humidity)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.frame_3 = QFrame(self.frame_controls)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
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


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout_5.addWidget(self.frame_controls)

        self.frame_middle = QFrame(self.frame_9)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setMinimumSize(QSize(320, 0))
        self.frame_middle.setMaximumSize(QSize(320, 16777215))
        self.frame_middle.setFrameShape(QFrame.NoFrame)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_middle)
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_consumption = QFrame(self.frame_middle)
        self.frame_consumption.setObjectName(u"frame_consumption")
        self.frame_consumption.setMinimumSize(QSize(0, 0))
        self.frame_consumption.setMaximumSize(QSize(16777215, 16777215))
        self.frame_consumption.setFrameShape(QFrame.NoFrame)
        self.frame_consumption.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_consumption)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top_frame_consumption = QFrame(self.frame_consumption)
        self.top_frame_consumption.setObjectName(u"top_frame_consumption")
        self.top_frame_consumption.setMinimumSize(QSize(0, 56))
        self.top_frame_consumption.setMaximumSize(QSize(16777215, 56))
        self.top_frame_consumption.setFrameShape(QFrame.NoFrame)
        self.top_frame_consumption.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.top_frame_consumption)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_consumption = QLabel(self.top_frame_consumption)
        self.label_consumption.setObjectName(u"label_consumption")

        self.horizontalLayout_19.addWidget(self.label_consumption)


        self.verticalLayout_9.addWidget(self.top_frame_consumption)

        self.main_frame_consumption = QFrame(self.frame_consumption)
        self.main_frame_consumption.setObjectName(u"main_frame_consumption")
        self.main_frame_consumption.setFrameShape(QFrame.NoFrame)
        self.main_frame_consumption.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.main_frame_consumption)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(15, 20, 15, 22)
        self.circular_cc_bg = QFrame(self.main_frame_consumption)
        self.circular_cc_bg.setObjectName(u"circular_cc_bg")
        self.circular_cc_bg.setMinimumSize(QSize(120, 120))
        self.circular_cc_bg.setMaximumSize(QSize(120, 120))
        self.circular_cc_bg.setFrameShape(QFrame.NoFrame)
        self.circular_cc_bg.setFrameShadow(QFrame.Raised)
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
        self.circular_cc_prog.setFrameShape(QFrame.NoFrame)
        self.circular_cc_prog.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.circular_cc_prog)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.circular_cc_main = QFrame(self.circular_cc_prog)
        self.circular_cc_main.setObjectName(u"circular_cc_main")
        self.circular_cc_main.setFrameShape(QFrame.NoFrame)
        self.circular_cc_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.circular_cc_main)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label = QLabel(self.circular_cc_main)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label)


        self.horizontalLayout_22.addWidget(self.circular_cc_main)


        self.horizontalLayout_21.addWidget(self.circular_cc_prog)


        self.horizontalLayout_20.addWidget(self.circular_cc_bg)

        self.frame_12 = QFrame(self.main_frame_consumption)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.kwh_consumption_label = QLabel(self.frame_12)
        self.kwh_consumption_label.setObjectName(u"kwh_consumption_label")
        self.kwh_consumption_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.kwh_consumption_label)

        self.kwh_max_label = QLabel(self.frame_12)
        self.kwh_max_label.setObjectName(u"kwh_max_label")
        self.kwh_max_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.kwh_max_label)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)


        self.horizontalLayout_20.addWidget(self.frame_12)


        self.verticalLayout_9.addWidget(self.main_frame_consumption)


        self.verticalLayout_8.addWidget(self.frame_consumption)

        self.frame_traffic = QFrame(self.frame_middle)
        self.frame_traffic.setObjectName(u"frame_traffic")
        self.frame_traffic.setMinimumSize(QSize(0, 50))
        self.frame_traffic.setFrameShape(QFrame.NoFrame)
        self.frame_traffic.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_traffic)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.top_frame_traffic = QFrame(self.frame_traffic)
        self.top_frame_traffic.setObjectName(u"top_frame_traffic")
        self.top_frame_traffic.setMinimumSize(QSize(0, 56))
        self.top_frame_traffic.setMaximumSize(QSize(16777215, 56))
        self.top_frame_traffic.setFrameShape(QFrame.NoFrame)
        self.top_frame_traffic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.top_frame_traffic)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_traffic = QLabel(self.top_frame_traffic)
        self.label_traffic.setObjectName(u"label_traffic")

        self.horizontalLayout_24.addWidget(self.label_traffic)


        self.verticalLayout_12.addWidget(self.top_frame_traffic)

        self.main_frame_traffic = QFrame(self.frame_traffic)
        self.main_frame_traffic.setObjectName(u"main_frame_traffic")
        self.main_frame_traffic.setFrameShape(QFrame.NoFrame)
        self.main_frame_traffic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.main_frame_traffic)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.traffic_chart = QLabel(self.main_frame_traffic)
        self.traffic_chart.setObjectName(u"traffic_chart")
        self.traffic_chart.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.traffic_chart)


        self.verticalLayout_12.addWidget(self.main_frame_traffic)


        self.verticalLayout_8.addWidget(self.frame_traffic)


        self.horizontalLayout_5.addWidget(self.frame_middle)

        self.frame_chart = QFrame(self.frame_9)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setFrameShape(QFrame.NoFrame)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_chart)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.frame_11 = QFrame(self.frame_chart)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 55))
        self.frame_11.setMaximumSize(QSize(16777215, 55))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.eletricity_button = QPushButton(self.frame_11)
        self.eletricity_button.setObjectName(u"eletricity_button")
        self.eletricity_button.setCheckable(True)
        self.eletricity_button.setChecked(True)

        self.horizontalLayout_16.addWidget(self.eletricity_button)

        self.devices_button = QPushButton(self.frame_11)
        self.devices_button.setObjectName(u"devices_button")
        self.devices_button.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.devices_button)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame_chart_main = QFrame(self.frame_chart)
        self.frame_chart_main.setObjectName(u"frame_chart_main")
        self.frame_chart_main.setFrameShape(QFrame.NoFrame)
        self.frame_chart_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_chart_main)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.eletricy_consumption_chart = QLabel(self.frame_chart_main)
        self.eletricy_consumption_chart.setObjectName(u"eletricy_consumption_chart")
        self.eletricy_consumption_chart.setMaximumSize(QSize(650, 400))
        self.eletricy_consumption_chart.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.eletricy_consumption_chart)


        self.verticalLayout_6.addWidget(self.frame_chart_main)


        self.horizontalLayout_5.addWidget(self.frame_chart)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.horizontalLayout_8.addWidget(self.left_main)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_frame.raise_()
        self.top_menu_frame.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hamburger_menu.setText("")
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"Modern IoT Dashboard PySide6", None))
        self.search_button.setText("")
        self.email_icon.setText("")
        self.notification_icon.setText("")
        self.user_pic.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"Luciano", None))
        self.temperature_button.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE", None))
        self.humidity_button.setText(QCoreApplication.translate("MainWindow", u"HUMIDITY", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700;\">0\u00b0</span></p></body></html>", None))
        self.celsius_label.setText(QCoreApplication.translate("MainWindow", u"Celsius", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.down_button.setText("")
        self.power_button.setText("")
        self.up_button.setText("")
        self.label_consumption.setText(QCoreApplication.translate("MainWindow", u"Solar Energy Consumption", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">42%</span></p></body></html>", None))
        self.kwh_consumption_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">6.421 kWh</span></p></body></html>", None))
        self.kwh_max_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\"font-size:13px; font-weight:600; color:#b4b4db; background-color:#323259;\">out of 8.421 kWh</span></p></body></html>", None))
        self.label_traffic.setText(QCoreApplication.translate("MainWindow", u"Traffic Consumption", None))
        self.traffic_chart.setText("")
        self.eletricity_button.setText(QCoreApplication.translate("MainWindow", u"ELETRICITY CONSUMPTION", None))
        self.devices_button.setText(QCoreApplication.translate("MainWindow", u"DEVICES", None))
        self.eletricy_consumption_chart.setText("")
    # retranslateUi

