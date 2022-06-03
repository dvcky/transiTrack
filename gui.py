import sys
import time
import PyQt5

from PyQt5 import QtWidgets, uic

#from qt_material import apply_stylesheet

print(QtWidgets.QStyleFactory.keys())

# CODE TO IMPORT .UI FILE
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('test.ui', self)

        self.pushButton.clicked.connect(self.buttonPress)
        self.show()

    def buttonPress(self):
        for i in range(101):
            self.progressBar.setValue(self.progressBar.value() + 1)
            time.sleep(0.01)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()