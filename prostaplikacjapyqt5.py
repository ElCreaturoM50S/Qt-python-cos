import sys
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maxwell")

        self.vboxlayout = QVBoxLayout()
        self.hboxlayout = QHBoxLayout()
        self.formlayout = QFormLayout()

        layout = self.hboxlayout
        """
        self.text = QLabel()
        self.checkbox = QCheckBox()
        self.radiobutton = QRadioButton()
        self.messagebox = QMessageBox()
        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
      
        widgets = [
            self.text,
            self.checkbox,
            self.radiobutton,
            self.messagebox,
            self.lineedit,
            self.spinbox
        ]

        for w in widgets:
            layout.addWidget(w)
        """


        self.edittext = GoofyAhhLabel()
        
        layout.addWidget(self.edittext)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

class GoofyAhhLabel(QLabel):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())