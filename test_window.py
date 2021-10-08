from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from untitled import Ui_MainWindow

class Layoutdemo(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Layoutdemo,self).__init__(parent)
        self.setupUi(self)

        self.actionClose.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.opmsg)
    def opmsg(self):
        file,ok=QFileDialog.getOpenFileName(self,"Open","c:/","ALL Files(*);;Text Files(*.Text)")
        self.statusbar.showMessage(file)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    ui=Layoutdemo()
    ui.show()
    sys.exit(app.exec_())