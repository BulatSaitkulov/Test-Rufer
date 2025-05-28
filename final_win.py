from instr import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from final_win import*

class finalWin(QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ex = ex 
        self.setAppear()
        self.initUI()
        self.show()
        

    def result(self):
        # ДОБАВИТЬ int к последнему
        # УБРАТЬ возраст. Он не суммируется
        self.index = (4* (int(self.ex.test1) + int(self.ex.test2) + int(self.ex.test3))-200)/10
        if self.ex.age >= 15:
            if self.index >= 15:
                return txt_res1
            if self.index >= 11 and self.index <= 14.9:
                return txt_res2
            if self.index >= 6 and self.index <= 10.9:
                return txt_res3
            if self.index >= 0.5 and self.index < 6: # граница
                return txt_res4
            if self.index <= 0.4:
                return txt_res5
        if self.ex.age >= 14 and self.ex.age <= 13: # из свойства ex
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
    #Устал дальше делать
    # Я дописала, можешь просто скопировать. С тебя тогда таймер) Все комменты для него написаны
        if self.ex.age == 7 or self.ex.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.ex.age == 9 or self.ex.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.ex.age == 11 or self.ex.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5

    def setAppear(self):
        self.setWindowTitle(txt_test2) # в скобочках заменить на переменную txt_title
        self.resize(win_x, win_y) # в скобочках заменить на переменную win_width, win_height
        self.move(win_width, win_height) # в скобочках заменить на переменную  (win_x, win_y
    
    def initUI(self):
        # вызывется функция
        self.workh_text = QLabel(txt_workheart + (self.result())) # ВЫЗЫВАЕМ функцию results а не work. Без str
        self.index = QLabel(txt_index + str(self.index))

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.workh_text, alignment =Qt.AlignCenter)# ДОБАВЛЕНЫ alignment =
        self.lay.addWidget(self.index, alignment =Qt.AlignCenter)
        self.setLayout(self.lay)
