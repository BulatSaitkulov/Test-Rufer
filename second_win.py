from instr import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from final_win import*
# ДОПИСАТЬ следующий импорты
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont 

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class secondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setAppear()
        self.initUI()
        self.connets()
        self.show()
    def setAppear(self):
        self.setWindowTitle(txt_title) # в скобочках заменить на переменную txt_title
        self.move(win_x, win_y) # в скобочках заменить на переменную win_width, win_height
        self.resize(win_width, win_height) # в скобочках заменить на переменную  (win_x, win_y
    
    def initUI(self):
        self.hLay = QHBoxLayout()
        self.rLay = QVBoxLayout()
        self.lLay = QVBoxLayout()

        # В QLineEdit убрать переменные
        self.name = QLabel(txt_name)
        self.enterName = QLineEdit()
        self.age = QLabel(txt_age)
        self.enterAge = QLineEdit()
        self.test1 = QLabel(txt_test1)
        self.button1 = QPushButton(txt_starttest1) # ДОБАВИТЬ переменную  txt_starttest1
        self.enterTest1 = QLineEdit()
        self.test2 = QLabel(txt_test2)
        self.button2 = QPushButton(txt_starttest2) # добавить переменные txt_starttest2
        self.enterTest2 = QLineEdit()
        self.test3 = QLabel(txt_test3)
        self.button3 = QPushButton(txt_starttest3) # добавить переменные txt_starttest3
        self.enterTest3 = QLineEdit() # ИЗМЕНИТЬ название
        self.text_timer = QLabel(txt_timer) # ДОБАВИТЬ переменные txt_timer и ИЗМЕНИТЬ название на text_timer
        
        self.buttonNext = QPushButton(txt_sendresults)

        # ДОБАВИТ просто чтобы красиво было. Добавляется текстовая подсказка
        self.enterName.setPlaceholderText(txt_hintname)
        self.enterAge.setPlaceholderText(txt_hintage)
        self.enterTest1.setPlaceholderText(txt_hinttest1)
        self.enterTest2.setPlaceholderText(txt_hinttest2)
        self.enterTest3.setPlaceholderText(txt_hinttest3)

        #  ИЗМЕНЕН правилный порядок и ДОБАВЛЕНО выравнивание по левому краю
        self.rLay.addWidget(self.name, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterName, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.age, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterAge, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.button1, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterTest1, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.button2, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.button3, alignment= Qt.AlignLeft) #это добавлено
        self.rLay.addWidget(self.enterTest2, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterTest3, alignment= Qt.AlignLeft) # изменено на правилное название
        self.rLay.addWidget(self.buttonNext, alignment= Qt.AlignCenter)  #это добавлено 


        self.lLay.addWidget(self.text_timer, alignment= Qt.AlignCenter)
        
        self.hLay.addLayout(self.rLay)
        self.hLay.addLayout(self.lLay)

        self.setLayout(self.hLay)  

    # ДОПИСАТЬ.
    '''
       Дам вам пример 1 таймера. timer_test и timer1Event.
       Для 2 и 3 таймера будут написаны названия функций, и комметарии. 
       2 и 3 таймер нужно ДОПИСАТЬ.
       В помощь слайды 1-30 для 1 таймера
                      32-38 для 2 и 3 таймера
    '''
    # функции для 1 таймера
    def timer_test(self):
       global time
       time = QTime(0, 0, 16) 
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer1Event)
       self.timer.start(1000)

    def timer1Event(self):
       global time
       time = time.addSecs(-1)
       self.text_timer.setText(time.toString("hh:mm:ss"))
       self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
       self.text_timer.setStyleSheet("color: rgb(0,0,0)")
       if time.toString("hh:mm:ss") == "00:00:00":
          self.timer.stop()
    # конец функций для 1 таймера


    # функции для 2 таймера
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    # конец функций для 2 таймера


    # функции для 3 таймера
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1500)


    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        secs = time.second()
        if secs >= 45 or secs <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

   # конец функций для 3 таймера

    def connets(self):
        self.buttonNext.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
        # ДОПИСАТЬ как на слайде 39
    
    def next_click(self):
        self.hide()
        # УБРАТЬ age и (). Должно быть так int(self.enterAge.text()) 
        # в конце оставить только  enterTest3
        self.ex = Experiment(int(self.enterAge.text()), self.enterTest1.text(), self.enterTest2.text(), self.enterTest3.text())        
        self.tw = finalWin(self.ex)
