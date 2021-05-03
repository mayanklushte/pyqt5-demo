import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Message Box")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        button = QPushButton('Click Me!', self)
        button.move(200, 150)
        button.setFont(font)
        button.clicked.connect(self.messagebox)

        self.show()

    def messagebox(self):
        # mbox = QMessageBox.question(self, "Warning", "Are You Sure to exit ?",
        #                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        # if mbox == QMessageBox.Yes:
        #     sys.exit()
        # elif mbox == QMessageBox.No:
        #     print('you clicked No')

        mbox = QMessageBox.information(self, 'Information', "You Loged Out")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
