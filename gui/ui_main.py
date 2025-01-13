# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 657)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1280, 800))
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
        self.top_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.top_menu_frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout = QHBoxLayout(self.top_menu_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.top_menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
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
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(self.top_menu_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.system_name = QLabel(self.frame_2)
        self.system_name.setObjectName(u"system_name")

        self.horizontalLayout_7.addWidget(self.system_name)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.top_menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(62, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
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
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.frame_6 = QFrame(self.top_menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(62, 16777215))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.notify_icon = QLabel(self.frame_6)
        self.notify_icon.setObjectName(u"notify_icon")
        self.notify_icon.setPixmap(QPixmap(u":/icons/resources/icons/bell-outline.svg"))
        self.notify_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.notify_icon)


        self.horizontalLayout.addWidget(self.frame_6)

        self.line_3 = QFrame(self.top_menu_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(1, 22))
        self.line_3.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.frame_7 = QFrame(self.top_menu_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(62, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.exit_icon = QLabel(self.frame_7)
        self.exit_icon.setObjectName(u"exit_icon")
        self.exit_icon.setPixmap(QPixmap(u":/icons/resources/icons/exit.svg"))
        self.exit_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.exit_icon)


        self.horizontalLayout.addWidget(self.frame_7)

        self.line_4 = QFrame(self.top_menu_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(1, 22))
        self.line_4.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.frame_8 = QFrame(self.top_menu_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(170, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.user_pic = QLabel(self.frame_8)
        self.user_pic.setObjectName(u"user_pic")
        self.user_pic.setMaximumSize(QSize(50, 50))
        self.user_pic.setPixmap(QPixmap(u":/icons/resources/icons/admin.svg"))
        self.user_pic.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.user_pic)

        self.user_name = QLabel(self.frame_8)
        self.user_name.setObjectName(u"user_name")

        self.horizontalLayout_6.addWidget(self.user_name)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.top_menu_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMaximumSize(QSize(1280, 800))
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.right_menu = QFrame(self.main_frame)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(251, 0))
        self.right_menu.setMaximumSize(QSize(251, 16777215))
        self.right_menu.setStyleSheet(u"")
        self.right_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.right_menu.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_8.addWidget(self.right_menu)

        self.left_main = QFrame(self.main_frame)
        self.left_main.setObjectName(u"left_main")
        self.left_main.setMaximumSize(QSize(1864, 16777215))
        self.left_main.setFrameShape(QFrame.Shape.NoFrame)
        self.left_main.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_main)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(36, 36, 36, 36)
        self.top_main_frame = QFrame(self.left_main)
        self.top_main_frame.setObjectName(u"top_main_frame")
        self.top_main_frame.setMaximumSize(QSize(16777215, 96))
        self.top_main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.top_main_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.top_main_frame)

        self.middle_main_frame = QFrame(self.left_main)
        self.middle_main_frame.setObjectName(u"middle_main_frame")
        self.middle_main_frame.setMaximumSize(QSize(16777215, 96))
        self.middle_main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.middle_main_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.middle_main_frame)

        self.frame_9 = QFrame(self.left_main)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_controls = QFrame(self.frame_9)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setMaximumSize(QSize(320, 16777215))
        self.frame_controls.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_controls.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_controls)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 0, 12, 12)
        self.frame_10 = QFrame(self.frame_controls)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 55))
        self.frame_10.setMaximumSize(QSize(16777215, 55))
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
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
        self.stackedWidget.addWidget(self.temperature)
        self.humidity = QWidget()
        self.humidity.setObjectName(u"humidity")
        self.stackedWidget.addWidget(self.humidity)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_controls)

        self.frame_middle = QFrame(self.frame_9)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setMinimumSize(QSize(320, 0))
        self.frame_middle.setMaximumSize(QSize(320, 16777215))
        self.frame_middle.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_middle.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_middle)
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_consumption = QFrame(self.frame_middle)
        self.frame_consumption.setObjectName(u"frame_consumption")
        self.frame_consumption.setMinimumSize(QSize(0, 0))
        self.frame_consumption.setMaximumSize(QSize(16777215, 16777215))
        self.frame_consumption.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_consumption.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_consumption)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top_frame_consumption = QFrame(self.frame_consumption)
        self.top_frame_consumption.setObjectName(u"top_frame_consumption")
        self.top_frame_consumption.setMinimumSize(QSize(0, 56))
        self.top_frame_consumption.setMaximumSize(QSize(16777215, 56))
        self.top_frame_consumption.setFrameShape(QFrame.Shape.NoFrame)
        self.top_frame_consumption.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.top_frame_consumption)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_consumption = QLabel(self.top_frame_consumption)
        self.label_consumption.setObjectName(u"label_consumption")

        self.horizontalLayout_19.addWidget(self.label_consumption)


        self.verticalLayout_9.addWidget(self.top_frame_consumption)

        self.main_frame_consumption = QFrame(self.frame_consumption)
        self.main_frame_consumption.setObjectName(u"main_frame_consumption")
        self.main_frame_consumption.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame_consumption.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.main_frame_consumption)


        self.verticalLayout_8.addWidget(self.frame_consumption)

        self.frame_traffic = QFrame(self.frame_middle)
        self.frame_traffic.setObjectName(u"frame_traffic")
        self.frame_traffic.setMinimumSize(QSize(0, 50))
        self.frame_traffic.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_traffic.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_traffic)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.top_frame_traffic = QFrame(self.frame_traffic)
        self.top_frame_traffic.setObjectName(u"top_frame_traffic")
        self.top_frame_traffic.setMinimumSize(QSize(0, 56))
        self.top_frame_traffic.setMaximumSize(QSize(16777215, 56))
        self.top_frame_traffic.setFrameShape(QFrame.Shape.NoFrame)
        self.top_frame_traffic.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.top_frame_traffic)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_traffic = QLabel(self.top_frame_traffic)
        self.label_traffic.setObjectName(u"label_traffic")

        self.horizontalLayout_24.addWidget(self.label_traffic)


        self.verticalLayout_12.addWidget(self.top_frame_traffic)

        self.main_frame_traffic = QFrame(self.frame_traffic)
        self.main_frame_traffic.setObjectName(u"main_frame_traffic")
        self.main_frame_traffic.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame_traffic.setFrameShadow(QFrame.Shadow.Raised)
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
        self.frame_chart.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_chart.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_chart)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.frame_11 = QFrame(self.frame_chart)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 55))
        self.frame_11.setMaximumSize(QSize(16777215, 55))
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.eletricity_button = QPushButton(self.frame_11)
        self.eletricity_button.setObjectName(u"eletricity_button")
        self.eletricity_button.setCheckable(True)
        self.eletricity_button.setChecked(True)

        self.horizontalLayout_16.addWidget(self.eletricity_button)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame_chart_main = QFrame(self.frame_chart)
        self.frame_chart_main.setObjectName(u"frame_chart_main")
        self.frame_chart_main.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_chart_main.setFrameShadow(QFrame.Shadow.Raised)
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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hamburger_menu.setText("")
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"Seva\u7a7a\u5f00\u63a7\u5236\u7cfb\u7edf", None))
        self.search_button.setText("")
        self.notify_icon.setText("")
        self.exit_icon.setText("")
        self.user_pic.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.temperature_button.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6", None))
        self.humidity_button.setText(QCoreApplication.translate("MainWindow", u"\u6e7f\u5ea6", None))
        self.label_consumption.setText(QCoreApplication.translate("MainWindow", u"\u7535\u91cf", None))
        self.label_traffic.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6d41", None))
        self.traffic_chart.setText("")
        self.eletricity_button.setText(QCoreApplication.translate("MainWindow", u"\u7535\u91cf\u7edf\u8ba1", None))
        self.eletricy_consumption_chart.setText("")
    # retranslateUi

