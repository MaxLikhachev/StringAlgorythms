import sys
from Naive import *
from PyQt5.QtWidgets import *
from termcolor import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)

        chooseAlgorythmNaive = QAction('Naive', self)
        chooseAlgorythmNaive.setStatusTip('Open new File')
        chooseAlgorythmNaive.triggered.connect(self.showNaiveAlgorytmDialog)
        fileMenu = menubar.addMenu('Algorythm')
        fileMenu.addAction(chooseAlgorythmNaive)

        self.setGeometry(300, 300, 650, 300)
        self.setWindowTitle('Entry string')
        self.show()


    def showFileDialog(self):
        file = open(QFileDialog.getOpenFileName(self, 'Open file', './')[0], 'r')
        with file: 
            self.textEdit.setText(file.read())


    def showNaiveAlgorytmDialog(self):
        if self.textEdit.toPlainText() == "": 
            self.statusBar().showMessage(str(colored('Entry string is empty','red')))
        else: 
            text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter pattern:')
            if ok:
                naive = Naive(self.textEdit.toPlainText(),text)
                self.statusBar().showMessage(naive.__str__())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())