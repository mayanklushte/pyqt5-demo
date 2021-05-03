import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Line Edit")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("please enter your name")
        self.nameTextBox.move(150, 50)
        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.setPlaceholderText("please enter your password")
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(150, 80)

        button = QPushButton("Save", self)
        button.move(150, 130)
        button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passwordTextBox.text()

        print(name, password)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
