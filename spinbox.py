import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 16)


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Message Box")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(150, 100)
        self.spinbox.setFont(font)
        # set range of spinbox
        # self.spinbox.setMinimum(1)
        # self.spinbox.setMaximum(120)
        self.spinbox.setRange(1, 1000)

        # use symbol in spinbox
        # prefix
        self.spinbox.setPrefix("$ ")
        # sufix
        # self.spinbox.setSuffix(" cm")

        # change stepsize of increses
        self.spinbox.setSingleStep(5)

        # get the value of spinbox

        # self.spinbox.valueChanged.connect(self.getValue)
        button = QPushButton("send", self)
        button.move(150, 140)
        button.clicked.connect(self.getValue)

        self.show()

    def getValue(self):
        value = self.spinbox.value()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
