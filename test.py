from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QWidget,QCheckBox
import sys
from Ui_main_window import *
class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
if __name__ =='__main__':
    app = QApplication(sys.argv)

    myWin=Window()
    myWin.show()
    
    sys.exit(app.exec_())