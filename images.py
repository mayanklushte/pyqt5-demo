import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using Images")
        self.setGeometry(150, 150, 550, 450)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/logo.png'))
        self.image.move(150, 50)
        removeButton = QPushButton("Remove", self)
        removeButton.move(150, 350)
        removeButton.clicked.connect(self.removeImage)
        showButton = QPushButton("Show", self)
        showButton.move(260, 350)
        showButton.clicked.connect(self.showImage)
        self.show()

    def removeImage(self):
        self.image.close()

    def showImage(self):
        self.image.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
