import sys
from algorythm import *
from PyQt5.QtWidgets import *

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

        chooseNaiveAlgorythm = QAction('Naive', self)
        chooseNaiveAlgorythm.triggered.connect(self.showNaiveAlgorythmDialog)

        chooseNaiveMaxBorderAlgorythm = QAction('NaiveMaxBorder', self)
        chooseNaiveMaxBorderAlgorythm.triggered.connect(self.showNaiveMaxBorderAlgorythmDialog)

        choosePrefixBorderArrayAlgorythm = QAction('PrefixBorderArray', self)
        choosePrefixBorderArrayAlgorythm.triggered.connect(self.showPrefixBorderArrayAlgorythmDialog)

        chooseSuffixBorderArrayAlgorythm = QAction('SuffixBorderArray', self)
        chooseSuffixBorderArrayAlgorythm.triggered.connect(self.showSuffixBorderArrayAlgorythmDialog)

        choosePrefixBorderArrayModifiedAlgorythm = QAction('PrefixBorderArrayModified', self)
        choosePrefixBorderArrayModifiedAlgorythm.triggered.connect(self.showPrefixBorderArrayModifiedAlgorythmDialog)

        fileMenu = menubar.addMenu('Algorythm')
        fileMenu.addAction(chooseNaiveAlgorythm)
        fileMenu.addAction(chooseNaiveMaxBorderAlgorythm)
        fileMenu.addAction(choosePrefixBorderArrayAlgorythm)
        fileMenu.addAction(chooseSuffixBorderArrayAlgorythm)
        fileMenu.addAction(choosePrefixBorderArrayModifiedAlgorythm)

        self.setGeometry(300, 300, 650, 300)
        self.setWindowTitle('Entry string')
        self.show()


    def showFileDialog(self):
        file = open(QFileDialog.getOpenFileName(self, 'Open file', './')[0], 'r')
        with file: 
            self.textEdit.setText(file.read())


    def isStringEmpty(self):
        isEmpty = self.textEdit.toPlainText() == ""
        if isEmpty:
            self.statusBar().showMessage(str('Entry string is empty'))
        return isEmpty


    def showNaiveAlgorythmDialog(self):
        if not self.isStringEmpty(): 
            text, ok = QInputDialog.getText(self, 'Enter pattern', 'Enter pattern:')
            if ok:
                self.statusBar().showMessage(Naive(self.textEdit.toPlainText(),text).__str__())


    def showNaiveMaxBorderAlgorythmDialog(self):
        if not self.isStringEmpty():
            self.statusBar().showMessage(NaiveMaxBorder(self.textEdit.toPlainText()).__str__())


    def showPrefixBorderArrayAlgorythmDialog(self):
        if not self.isStringEmpty():
            self.statusBar().showMessage(PrefixBorderArray(self.textEdit.toPlainText()).__str__())


    def showSuffixBorderArrayAlgorythmDialog(self):
        if not self.isStringEmpty():
            self.statusBar().showMessage(SuffixBorderArray(self.textEdit.toPlainText()).__str__())
    

    def showPrefixBorderArrayModifiedAlgorythmDialog(self):
        if not self.isStringEmpty():
            self.statusBar().showMessage(PrefixBorderArrayModified(self.textEdit.toPlainText()).__str__())
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())