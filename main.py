import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QWidget, QFrame, QSpacerItem, QSizePolicy
from PySide6.QtGui import QColor, QPixmap, QIcon
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize,QTimer
from PySide6.QtSvgWidgets import QSvgWidget

from gui.ui_main import Ui_MainWindow
from gui.ui_card_component import Ui_CardComponent
from gui.ui_circular_controler import Ui_CircularControler
from gui.ui_consumption import Ui_Consumption

import mantun
import os 
import sys 
import argparse

def ensure_single_instance(pid_file='/tmp/iot-mantun.pid'):
    if os.path.exists(pid_file):
        with open(pid_file,'r') as f:
            pid=int(f.read().strip())
        try:
            os.kill(pid,0)
            print('Another instance is already running')
            sys.exit(1)
        except OSError:
            pass 
    
    with open(pid_file,'w') as f:
        f.write(str(os.getpid()))

parser=argparse.ArgumentParser(description='Mantun IOT')
parser.add_argument('--port',default='/dev/ttyS4')
parser.add_argument('--pid_file',default='/tmp/iot-mantun.pid')

args=parser.parse_args()
print(f'[debug] pid_file:{args.pid_file} port:{args.port}') 
 
ensure_single_instance(pid_file=args.pid_file)

class Consumption(QWidget, Ui_Consumption):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class CircularControler(QWidget, Ui_CircularControler):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.value = 0
        self.current_state = True
        self.updated_stylesheet = ""
        
        down_layout = QHBoxLayout()
        up_layout = QHBoxLayout()
        power_layout = QHBoxLayout()
             
        self.up_button.clicked.connect(lambda: self.define_temperature("up"))
        self.down_button.clicked.connect(lambda: self.define_temperature("down"))
        
        self.power_button.clicked.connect(self.power)
        
        down_layout.addWidget(QSvgWidget("resources/icons/arrow-downward-outline.svg"))
        up_layout.addWidget(QSvgWidget("resources/icons/arrow-upward-outline.svg"))
        power_layout.addWidget(QSvgWidget("resources/icons/power-outline.svg"))
        
        self.down_button.setLayout(down_layout)
        self.up_button.setLayout(up_layout)
        self.power_button.setLayout(power_layout)
        
    def power(self):
        if self.current_state:
            self.circular_prog.setStyleSheet("")
            self.temperature_label.setText('<html><head/><body><p><span style=" font-size:36pt; font-weight:700;"> -- </span></p></body></html>')
            self.down_button.setEnabled(False)
            self.up_button.setEnabled(False)
            self.current_state = False
            return
        else:
            self.text_base = '<html><head/><body><p><span style=" font-size:36pt; font-weight:700;">{}°</span></p></body></html>'.format(str(self.value))
            self.circular_prog.setStyleSheet(self.updated_stylesheet)
            self.temperature_label.setText(self.text_base)
            self.down_button.setEnabled(True)
            self.up_button.setEnabled(True)
            self.current_state = True
            return
        
    def define_temperature(self, direction):
        if direction == "up" and self.value < 100:
            self.value  += 10
        elif direction == "down" and self.value > 0:
            self.value -= 10
        
        self.stop_1 = (1 - ((self.value / 100)) - 0.01)
        self.stop_2 = (1 - ((self.value / 100)))
        
        stylesheet_base = """
        QFrame#circular_prog
        {
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:271, stop:{STOP_1} rgba(127, 169, 251, 0), stop:{STOP_2} rgba(238, 255, 0, 255));
            border-radius: 125px;
        }
        """
        
        self.updated_stylesheet = stylesheet_base.replace("{STOP_1}",str(self.stop_1)).replace("{STOP_2}", str(self.stop_2))
        
        self.circular_prog.setStyleSheet(self.updated_stylesheet)
        
        self.text_base = '<html><head/><body><p><span style=" font-size:36pt; font-weight:700;">{}°</span></p></body></html>'.format(str(self.value))
        self.temperature_label.setText(self.text_base)

class CustomButton(QPushButton):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.setStyleSheet("""
                           min-height: 48px;
                           border: none;
                           border-bottom: 1px solid rgb(31, 31, 64);
                           text-align: left;
                           padding-left: 18px;
                           font-weight: 600;
                           """)
        self.setText(kwargs.get("text"))
        self.setIcon(QIcon(kwargs.get("icon")))
        self.setIconSize(QSize(20, 20))

class CardComponent(QWidget, Ui_CardComponent):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        
        # if 'frame_svg_color_1' in kwargs and 'frame_svg_color_2' in kwargs:
        #     self.frame.setStyleSheet("QFrame#card_frame_svg{background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 %s, stop:1 %s);border-radius:10px}" % (kwargs.get('frame_svg_color_1'), kwargs.get('frame_svg_color_2')))

        # self.svg  = QSvgWidget(kwargs.get('svg_path'))
        # self.svg.setMaximumSize(35, 35)
        
        # self.frame_svg_layout = QHBoxLayout()
        
        # self.frame_svg_layout.addWidget(self.svg)
        # self.card_frame_svg.setLayout(self.frame_svg_layout)
        
        self.card_text.setText(kwargs.get('title'))
        
        # if not kwargs.get('button'):
        #     self.card_button.hide()
        # else:
        #     self.card_button.setText(kwargs.get('button'))
        
        self.horizontalLayout = QHBoxLayout()
        self.frame.setLayout(self.horizontalLayout)
        
    def setText(self,text):
        self.card_text.setText(text)    

class MainWindow(QMainWindow, Ui_MainWindow):
    def exitMousePressEvent(self,event):
        self.close()
    
    def __init__(self,port='/dev/ttyS4'):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowFlag(Qt.Window | Qt.CustomizeWindowHint)

        self.frame_7.mousePressEvent=self.exitMousePressEvent
        
        # self.resize(1920, 1080)
        self.showMaximized()
        
        # Add a shadow on frame color black
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(80)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        self.top_menu_frame.setGraphicsEffect(self.shadow)
        
        self.hamburger_menu.clicked.connect(self.toggle_menu)
        
        self.card_component_1 = CardComponent( title="总路")
        self.card_component_2 = CardComponent(title="1路")
        self.card_component_3 = CardComponent( title="2路")
        self.card_component_4 = CardComponent( title="3路")
        self.card_component_5 = CardComponent(title="4路")
        self.card_component_6 = CardComponent(title="5路")

        self.card_component_1.card_button.clicked.connect(lambda checked:self.mantunSwitch(0,checked))
        self.card_component_2.card_button.clicked.connect(lambda checked:self.mantunSwitch(1,checked))
        self.card_component_3.card_button.clicked.connect(lambda checked:self.mantunSwitch(2,checked))
        self.card_component_4.card_button.clicked.connect(lambda checked:self.mantunSwitch(3,checked))
        self.card_component_5.card_button.clicked.connect(lambda checked:self.mantunSwitch(4,checked))
        self.card_component_6.card_button.clicked.connect(lambda checked:self.mantunSwitch(5,checked))
        self.search_button.clicked.connect(self.mantunRefresh)

        self.form_layout_1=QHBoxLayout()
        self.form_layout_1.addWidget(self.card_component_1)
        self.form_layout_1.addWidget(self.card_component_2)
        self.form_layout_1.addWidget(self.card_component_3)
        self.top_main_frame.setLayout(self.form_layout_1)
        self.top_main_frame.layout().setContentsMargins(0, 0, 0, 0)
        self.top_main_frame.layout().setSpacing(30)

        self.form_layout_2 = QHBoxLayout()
        self.form_layout_2.addWidget(self.card_component_4)
        self.form_layout_2.addWidget(self.card_component_5)
        self.form_layout_2.addWidget(self.card_component_6)
 
        self.middle_main_frame.setLayout(self.form_layout_2)
        self.middle_main_frame.layout().setContentsMargins(0, 0, 0, 0)
        self.middle_main_frame.layout().setSpacing(30)
        
        self.temperature_button.clicked.connect(self.temperature_page)
        self.humidity_button.clicked.connect(self.humidity_page)
        
        self.chart_frame_layout = QHBoxLayout()
        self.chart_frame_layout.addWidget(QSvgWidget("resources/images/visualization.svg"))
        
        self.frame_chart_main.setLayout(self.chart_frame_layout)
        
        self.circular_temp_layout = QVBoxLayout()
        self.circular_temp = CircularControler()
        self.temperature.setLayout(self.circular_temp_layout)
        self.temperature.layout().addWidget(self.circular_temp)
        
        self.circular_humi_layout = QVBoxLayout()
        self.circular_humi = CircularControler()
        self.humidity.setLayout(self.circular_humi_layout)
        self.humidity.layout().addWidget(self.circular_humi)
        
        self.traffic_chart.setPixmap(QPixmap("resources/images/traffic.png"))
        self.eletricy_consumption_chart.setPixmap(QPixmap("resources/images/eletricity.png"))
        
        #Add custom buttons on menu
        
        self.buttons_layout = QVBoxLayout()
        
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.iot_dashboard_button = CustomButton(
            icon="resources/icons/home-outline.svg",
            text="仪表板"
        )
         
        
        self.buttons_layout.addWidget(self.iot_dashboard_button) 
         
        
        self.buttons_layout.addItem(self.spacer)
        
        self.right_menu.setLayout(self.buttons_layout)
        self.right_menu.layout().setContentsMargins(0, 0, 0, 0)
        
        
        self.consumption_layout = QVBoxLayout()
        self.consumption_widget = Consumption()
        self.main_frame_consumption.setLayout(self.consumption_layout)
        self.main_frame_consumption.layout().addWidget(self.consumption_widget)

        self.mantunModbus(port=port)
        self.timer=QTimer()
        self.timer.timeout.connect(self.mantunRefreshTask)
        self.timer.start(3000)
        
    def temperature_page(self):
            self.stackedWidget.setCurrentIndex(0)
            self.temperature_button.setChecked(True)
            self.humidity_button.setChecked(False)

    def humidity_page(self):
            self.stackedWidget.setCurrentIndex(1)
            self.humidity_button.setChecked(True)
            self.temperature_button.setChecked(False)
        
    def toggle_menu(self):
        if self.right_menu.width() == 251:
            new_width = 56
            self.iot_dashboard_button.setText('')
        else:
            new_width = 251
            self.iot_dashboard_button.setText('仪表板')
            
        self.animation = QPropertyAnimation(self.right_menu, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()

    def mantunModbus(self,port):
        try:
            self.mantunLock=threading.Lock()
            self.mantunModbus=mantun.MantunModbus(port=port,timeout=2) 
        except Exception as e:
            print(f'[failed] connect modbus failed {e}')
            self.mantunModbus=None 
            return 
        self.mantunRefresh()

    def setCardButton(self,cardNo,checked:bool):
        if cardNo==0:
            self.card_component_1.card_button.setChecked(checked)
        elif cardNo== 1:
            self.card_component_2.card_button.setChecked(checked)
        elif cardNo== 2:
            self.card_component_3.card_button.setChecked(checked)
        elif cardNo== 3:
            self.card_component_4.card_button.setChecked(checked)
        elif cardNo==4:
            self.card_component_5.card_button.setChecked(checked)
        elif cardNo== 5:
            self.card_component_6.card_button.setChecked(checked)    
    def mantunSwitch(self,switchNo,checked:bool):
        if self.mantunModbus is None:
            return 
        try:
            self.mantunLock.acquire()
            self.timer.stop()
            # print(f'[info] switch {switchNo} {checked}')
            state=self.mantunModbus.switch(switchNo=switchNo,switch=checked)
            self.setCardButton(state['switchNo'],state['switch'])
        except Exception as e:
            self.setCardButton(switchNo,not checked)          
            print(f'[error] switch {switchNo} failed {e}')
        finally:
            self.mantunLock.release()
            self.timer.start(3000)
    
    def mantunRefresh(self):
        if self.mantunModbus is None:
            return 
        if self.mantunLock.locked():
            return 
        try:
            self.mantunLock.acquire()
            states=self.mantunModbus.readSwitchState()
            for state in states:
                self.setCardButton(state['switchNo'],state['switch'])
        except Exception as e:
            print(f'[error] readSwitchState failed {e}')
        finally:
            self.mantunLock.release()
    
    def mantunRefreshTask(self):
        threading.Thread(target=self.mantunRefresh).start()

app = QApplication([])

window = MainWindow(port=args.port)
window.show()

app.exec()
