from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()

        self.exp = exp

        self.initUI()

        self.set_appear()


        self.show()

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "Данные для этого возроста отсутствуют"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        # для возраста 7 - 8 лет
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1 
            
            elif 21 > self.index >= 17:
                return txt_res2

            elif 17 > self.index >= 12:
                return txt_res3

            elif 12 > self.index >= 6.5:
                return txt_res4
            
            else:
                return txt_res5
            
        # для возраста 9 - 10 лет
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1 
            
            elif 19.5 > self.index >= 15.5:
                return txt_res2

            elif 15.5 > self.index >= 10.5:
                return txt_res3

            elif 10.5 > self.index >= 5:
                return txt_res4
            
            else:
                return txt_res5
        
        # для возраста 11 - 12 лет
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 18:
                return txt_res1 
            
            elif 18 > self.index >= 14:
                return txt_res2

            elif 14 > self.index >= 9:
                return txt_res3

            elif 9 > self.index >= 3.5:
                return txt_res4
            
            else:
                return txt_res5
        
        # для возраста 13 - 14 лет
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 16.5:
                return txt_res1 
            
            elif 16.5 > self.index >= 12.5:
                return txt_res2

            elif 12.5 > self.index >= 7.5:
                return txt_res3

            elif 7.5 > self.index >= 2:
                return txt_res4
            
            else:
                return txt_res5
        
        # для возраста от 15
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1 
            
            elif 15 > self.index >= 11:
                return txt_res2

            elif 11 > self.index >= 6:
                return txt_res3

            elif 6 > self.index >= 0.5:
                return txt_res4
            
            else:
                return txt_res5


    def initUI(self):
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_txt = QLabel(txt_index + str(self.index))

        self.layout_line = QVBoxLayout()

        self.layout_line.addWidget(self.index_txt, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)

        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)