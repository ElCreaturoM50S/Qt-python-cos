import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("amonger")
        
        self.text = QLabel(self)
        self.text.setText('bruh bruh')
    def change_text(self):
        self.text.setText('Tekst 2')

if __name__ == '__main__':
        app = QApplication(sys)
        main = Main()
        main.show()

        sys.exit(app.exec_())