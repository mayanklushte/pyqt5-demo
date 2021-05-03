import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Using List Widget")
        self.setGeometry(50, 50, 550, 550)
        self.UI()

    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)
        list1 = ['batman', 'superman', 'spiderman']
        self.listWidget.addItems(list1)
        self.listWidget.addItem('Heman')

        # for i in range(1, 23):
        #     self.listWidget.addItem(str(i))

        addbtn = QPushButton("Add", self)
        addbtn.move(360, 80)
        addbtn.clicked.connect(self.addfunc)
        deletebtn = QPushButton("Delete", self)
        deletebtn.move(360, 110)
        deletebtn.clicked.connect(self.deletefuc)
        getbtn = QPushButton("Get", self)
        getbtn.move(360, 140)
        getbtn.clicked.connect(self.getbtnfunc)
        deleteallbtn = QPushButton("Delete All", self)
        deleteallbtn.move(360, 170)
        deleteallbtn.clicked.connect(self.deleteallfunc)

        self.show()

    def addfunc(self):
        value = self.addRecord.text()
        self.listWidget.addItem(value)
        self.addRecord.setText("")

    def deletefuc(self):
        id = self.listWidget.currentRow()
        self.listWidget.takeItem(id)

    def getbtnfunc(self):
        id = self.listWidget.currentItem().text()
        print(id)

    def deleteallfunc(self):
        self.listWidget.clear()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
