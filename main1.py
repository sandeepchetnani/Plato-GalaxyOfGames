from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from pygame.locals import *
from pygame import mixer

class Ui_MainWindow(object):
    mixer.init()
    mixer.music.load('background.wav')
    mixer.music.play()
    def snake1(self):
        import snakegame
    def tictactoe1(self):
        from tictactoes import tictactoe
    def gbs1(self):
        from GhostBusters import s
    def car1(self):
        from cars import car
    def ludo1(self):
        from ludo import ludoGame
    def flappybird(self):
        from FlappyBird import flap
    def aero(self):
        from Aeroblasters import aero
    def angrywalls(self):
        from AngryWalls import angry
    def dino(self):
        from Dino import dino
    def mp(self):
        from MemoryPuzzle import mp
    def pong(self):
        from Pong import pong
    def tetris(self):
        from Tetris import tetris
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 635)
        MainWindow.setStyleSheet("border-image: url(:/newPrefix/5.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 50, 111, 101))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/gs.jpg);")
        self.pushButton.setText("")
        self.pushButton.clicked.connect(self.gbs1)
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 50, 111, 101))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/snake1.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.clicked.connect(self.snake1)
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 50, 111, 101))
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/ludo.jpg);")
        self.pushButton_3.setText("")
        self.pushButton_3.clicked.connect(self.ludo1)
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 200, 111, 101))
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/cr.jpg);")
        self.pushButton_4.setText("")
        self.pushButton_4.clicked.connect(self.car1)
        self.pushButton_4.setObjectName("pushButton_4")
        
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 200, 111, 101))
        self.pushButton_5.setStyleSheet("\n"
"border-image: url(:/newPrefix/memory.png);")
        self.pushButton_5.clicked.connect(self.mp)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 350, 111, 101))
        self.pushButton_6.setStyleSheet("border-image: url(:/newPrefix/flappy.jpg);")
        self.pushButton_6.setText("")
        self.pushButton_6.clicked.connect(self.flappybird)
        self.pushButton_6.setObjectName("pushButton_6")
        
        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 350, 111, 101))
        self.pushButton_7.setStyleSheet("border-image: url(:/newPrefix/pong.jpg);")
        self.pushButton_7.setText("")
        self.pushButton_7.clicked.connect(self.pong)
        self.pushButton_7.setObjectName("pushButton_7")
        
        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 350, 111, 101))
        self.pushButton_8.setStyleSheet("\n"
"border-image: url(:/newPrefix/aero.png);")
        self.pushButton_8.setText("")
        self.pushButton_8.clicked.connect(self.aero)
        self.pushButton_8.setObjectName("pushButton_8")
        
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 500, 111, 101))
        self.pushButton_9.setStyleSheet("border-image: url(:/newPrefix/dino.jpg);")
        self.pushButton_9.setText("")
        self.pushButton_9.clicked.connect(self.dino)
        self.pushButton_9.setObjectName("pushButton_9")
        
        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 200, 111, 101))
        self.pushButton_10.setStyleSheet("border-image: url(:/newPrefix/ttt.png);")
        self.pushButton_10.setText("")
        self.pushButton_10.clicked.connect(self.tictactoe1)
        self.pushButton_10.setObjectName("pushButton_10")
        
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 500, 111, 101))
        self.pushButton_11.setStyleSheet("border-image: url(:/newPrefix/tetris.jpeg);")
        self.pushButton_11.setText("")
        self.pushButton_11.clicked.connect(self.tetris)
        self.pushButton_11.setObjectName("pushButton_11")
        
        
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(580, 500, 111, 101))
        self.pushButton_12.setStyleSheet("border-image: url(:/newPrefix/angrybird.png);")
        self.pushButton_12.setText("")
        self.pushButton_12.clicked.connect(self.angrywalls)
        self.pushButton_12.setObjectName("pushButton_12")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plato:Computer of Galaxy Games"))
import text


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
