import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("amonger")
        
        self.text = QLabel(self)
        self.text.setStyleSheet("color: red; font-size:15px")
        self.text.setText('bruh bruh')
        self.text.move(50,30)

        self.btgColor = QButtonGroup()
        self.rbtRed = QRadioButton("Red", self)
        self.rbtRed.move(50,50)
        self.rbtRed.setChecked(True)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtRed)

        self.rbtGreen = QRadioButton("Green", self)
        self.rbtGreen.move(50,80)
        self.rbtGreen.setChecked(True)

        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtGreen)
    def evt_rbt_clicked(self):
        msgBox = QMessageBox()
        msgBox.setText("witam witam witam")
        msgBox.exec()


if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = Main()
        main.show()

        sys.exit(app.exec_())