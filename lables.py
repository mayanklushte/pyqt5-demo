import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Lables")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        lable1 = QLabel('Hello Users', self)
        lable2 = QLabel('Hello mayank', self)
        lable1.move(100, 50)
        lable2.move(200, 50)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
