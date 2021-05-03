import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Checkbox")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('enter your name')
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText('enter your surname')
        self.name.move(150, 50)
        self.surname.move(150, 80)

        self.remember = QCheckBox("Remember Me", self)
        self.remember.move(150, 110)
        submit = QPushButton('submit', self)
        submit.move(200, 140)
        submit.clicked.connect(self.submitfunc)

        self.show()

    def submitfunc(self):

        if self.remember.isChecked():
            name = self.name.text()
            surname = self.surname.text()
            print(f'Name: {name} \nsurname: {surname} \nRemember me checked')
        else:
            name = self.name.text()
            surname = self.surname.text()
            print(
                f'Name: {name} \nsurname: {surname} \nRemember me not checked')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
