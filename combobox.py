import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Combo Box")
        self.setGeometry(250, 150, 550, 550)
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        self.combo.addItem("Python")
        self.combo.addItems(['C', "C++", "JAVA", "PHP"])
        button = QPushButton('save', self)
        button.move(150, 140)
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.combo.currentText()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
