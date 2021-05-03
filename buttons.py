import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Buttons")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.lable1 = QLabel('Hello Users', self)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton('Exit', self)

        self.lable1.move(100, 50)
        enterButton.move(100, 80)
        exitButton.move(200, 80)

        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.lable1.setText("You Clicked Enter")
        self.lable1.resize(150, 20)

    def exitFunc(self):
        self.lable1.setText("You Cliked Exit")
        self.lable1.resize(150, 20)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
