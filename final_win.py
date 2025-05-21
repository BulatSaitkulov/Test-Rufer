from instr import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from final_win import*

class finalWin(QWidget):
    def __init__(self):
        super().__init__(self, ex)
        self.setAppear()
        self.initUI()
        self.show()
        self.ex = ex

    def result(self):
        self.index = (4*(int(self.ex.age)+ int(self.ex.test1) + int(self.ex.test2) + (self.ex.test3))-200)/10
        if self.ex.age >= 15:
            if self.index >= 15:
                return txt_res1
            if self.index >= 11 and self.index <= 14.9:
                return txt_res2
            if self.index >= 6 and self.index <= 10.9:
                return txt_res3
            if self.index >= 0.5 and self.index <= 0.5:
                return txt_res4
            if self.index <= 0.4:
                return txt_res5
        if self.ex.age >= 14 and self.age <= 13:
            if self.index >= 16.5:
                return txt_res1
            if self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            if self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            if self.index >= 2 and self.index <= 7.4:
                return txt_res4
            if self.index <= 1.9:
                return txt_res5

    def setAppear(self):
        self.setWindowTitle(txt_test2)
        self.resize(win_x, win_y)
        self.move(win_width, win_height)
    def initUI(self):
        self.workh_text = QLabel(txt_workheart+str(self.work))
        self.index = QLabel(txt_index+str(self.index))

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.workh_text, Qt.AlignCenter)
        self.lay.addWidget(self.index, Qt.AlignCenter)
    
    def nextClick(self):
        self.hide()

