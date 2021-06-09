from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QMessageBox


class UIFunctions(QMainWindow):
    def __init__(self):
        super().__init__()

    # 페이지 전환 기능
    def showpage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.label_title_bar_top.setText("K-CocktailMate")

    def showhomepage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.ui.label_title_bar_top.setText("HOME")

    def showmonitor(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_monitor)
        self.ui.label_title_bar_top.setText("MONITOR")

    def showparameter(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_parameter)
        self.ui.label_title_bar_top.setText("PARAMETER")

    def showsetting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
        self.ui.label_title_bar_top.setText("SETTING")

    def replace_drink1(self):
        self.amount_sso = 360
        self.ui.drink1_progressbar.setValue(self.amount_sso/360 * 100)
        self.ui.drink1_residual_label.setText(str(self.amount_sso)+"ml")

    def replace_drink2(self):
        self.amount_mac = 500
        self.ui.drink2_progressbar.setValue(self.amount_mac/500 * 100)
        self.ui.drink2_residual_label.setText(str(self.amount_mac)+"ml")

    def temperature_up(self):
        self.target_temp += 1
        self.SharedMemory[1] = self.target_temp
        self.ui.set_temperature_qlcd.display(str(self.target_temp))

    def temperature_down(self):
        self.target_temp -= 1
        self.SharedMemory[1] = self.target_temp
        self.ui.set_temperature_qlcd.display(str(self.target_temp))

    def pump1_parameter_calculate(self, number):
        self.amount_per_sec_sso += number
        self.ui.pump1_parameter.display(str(round(self.amount_per_sec_sso, 2)))

    def pump2_parameter_calculate(self, number):
        self.amount_per_sec_mac += number
        self.ui.pump2_parameter.display(str(round(self.amount_per_sec_mac, 2)))
    
    def update_prograssbar(self):
        self.ui.beer_progressbar_2.setValue(self.ui.beer_slider.value())
        self.ui.beer_progressbar.setValue(100 - self.ui.beer_slider.value())
        
    # 오류 팝업    poped1 연결
    def show_popup(self, error_code):
        if error_code == 1:
            msg = QMessageBox()         # pump error
            msg.setWindowTitle("오류 발생")
            msg.setText("펌프에서 문제가 발생했습니다.")
            x = msg.exec_()
        elif error_code == 2:            # shortage
            msg = QMessageBox()
            msg.setWindowTitle("음료 부족")
            msg.setText("음료가 부족합니다.")
            x = msg.exec_()
        elif error_code == 3:
            msg = QMessageBox()
            msg.setWindowTitle("음료 부족")
            msg.setText("맥주가 부족합니다.")
        elif error_code == 4:
            msg = QMessageBox()
            msg.setWindowTitle("음료 부족")
            msg.setText("소주와 맥주가 부족합니다.")
        elif error_code == 5:
            msg = QMessageBox()
            msg.setWindowTitle("음료 부족")
            msg.setText("소주가 부족합니다.")
        elif error_code == 6:
            msg = QMessageBox()
            msg.setWindowTitle("음료 부족")
            msg.setText("소주와 맥주가 부족합니다.")
        elif error_code == 0:
            self.ui.drink1_residual_label.setText(str(int(self.amount_sso)))
            self.ui.drink2_residual_label.setText(str(int(self.amount_mac)))
            self.ui.drink1_progressbar.setValue(self.amount_sso/360 * 100)
            self.ui.drink2_progressbar.setValue(self.amount_mac/500 * 100)
        self.ui.start_button.setEnabled(True)
