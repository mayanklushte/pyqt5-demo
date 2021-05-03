import sys 
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setGeometry(150, 250, 550, 450)
        self.setWindowTitle("ERP")

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
    