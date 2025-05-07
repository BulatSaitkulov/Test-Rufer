from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout

class secondWin(QWidget):
    def setAppear(self):
        self.setWindowTitle(txt_test2)
        self.resize(win_x, win_y)
        self.move(win_width, win_height)
    def initUI(self):
        self.hLay = QHBoxLayout()
        self.rLay = QVBoxLayout()
        self.lLay = QVBoxLayout()

        self.lLay.addWidget()
        self.rLay.addWidget()
        
        self.hLay.addLayout(self.lLay)
        self.hLay.addLayout(self.rLay)

        self.widget.setLayout(hLay)



        

