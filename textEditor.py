import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Text Editor")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(120, 20)

        button = QPushButton('Send', self)
        button.move(230, 280)
        button.clicked.connect(self.getValues)

        self.show()

    def getValues(self):
        text = self.editor.toPlainText()
        print(text)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
