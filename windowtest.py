import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5

class Mainwindow(QMainWindow):
    def __init__(self,parent=None):
        super(Mainwindow,self).__init__(parent)
        self.resize(800,600)
        self.status=self.statusBar()
        self.status.showMessage("状态栏提示",5000)
        self.setWindowTitle("主窗口")
        screen=QDesktopWidget().screenGeometry()
        self.button=QPushButton("OPEN")
        self.button.clicked.connect(self.showdialog)
        self.line=QLineEdit()
        self.line.setPlaceholderText("hello")
        self.line.setEchoMode(QLineEdit.Password)
        self.line.setMaxLength(10)
        self.com=QComboBox()
        for i in range(4):
            self.com.addItem(str(i))
        layout=QVBoxLayout()
        self.le=QLabel()
        self.contetx=QTextEdit()
        self.cal=QCalendarWidget()
        self.model=QStandardItemModel(4,4)
        self.model.setHorizontalHeaderLabels(["1",'2','3','4'])
        for i in range(4):
            for j in range(4):
                item=QStandardItem(str(i)+str(j))
                self.model.setItem(i,j,item)
        self.t=QTableView()
        self.t.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.t.setModel(self.model)
        layout.addWidget(self.t)

        layout.addWidget(self.button)
        layout.addWidget(self.line)
        layout.addWidget(self.com)
        layout.addWidget(self.cal)
        layout.addWidget(self.contetx)
        mainform=QWidget()
        mainform.setLayout(layout)
        self.setCentralWidget(mainform)

        self.setWindowIcon(QIcon("Monitor.ico"))
        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("this is a example <hr>")
        bar=self.menuBar()
        file=bar.addMenu("file")
        new=file.addAction("new")
        new=QAction("Quit",self)
        a=self.addToolBar("g")
    def showdialog(self):
        dlg=QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            f=dlg.selectedFiles()
            a=open(f[0],"r")
            with a:
                d=a.read()

                if d=="":
                    self.contetx.setText("No content!")
                self.contetx.setText(d)




if __name__=="__main__":
    app=QApplication(sys.argv)
    form=Mainwindow()
    form.show()
    sys.exit(app.exec_())