import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Radio Button")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(150, 50)
        self.name.setPlaceholderText("please enter name")
        self.surname = QLineEdit(self)
        self.surname.move(150, 80)
        self.surname.setPlaceholderText("please enter surname")

        self.male = QRadioButton("Male", self)
        self.male.setChecked(True)
        self.male.move(150, 110)
        self.female = QRadioButton("Female", self)
        self.female.move(220, 110)
        button = QPushButton('sunmit', self)
        button.clicked.connect(self.getValues)
        button.move(200, 140)

        self.show()

    def getValues(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print(f' Name: {name} \n Surname: {surname} \n Gender: Male ')
        else:
            print(f' Name: {name} \n Surname: {surname} \n Gender: Female ')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
