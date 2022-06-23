import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(270, 270))

        self.setWindowTitle('Kalkulator')

        layout = QGridLayout()

        self.input = QLineEdit()
        self.input.setReadOnly(True) # pole tylko do odczytu


        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button10 = QPushButton("÷")

        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button11 = QPushButton("×")

        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button12 = QPushButton("-")

        self.button0 = QPushButton("0")
        self.button13 = QPushButton(".")
        self.button14 = QPushButton("+")

        self.buttonC = QPushButton("C")
        self.button15 = QPushButton("=")


        # C L I C K E D
        self.button7.clicked.connect(lambda: self.wpisz7())
        self.button8.clicked.connect(lambda: self.wpisz8())
        self.button9.clicked.connect(lambda: self.wpisz9())
        self.button10.clicked.connect(lambda: self.dzielenie())

        self.button4.clicked.connect(lambda: self.wpisz4())
        self.button5.clicked.connect(lambda: self.wpisz5())
        self.button6.clicked.connect(lambda: self.wpisz6())
        self.button11.clicked.connect(lambda: self.mnozenie())

        self.button1.clicked.connect(lambda: self.wpisz1())
        self.button2.clicked.connect(lambda: self.wpisz2())
        self.button3.clicked.connect(lambda: self.wpisz3())
        self.button12.clicked.connect(lambda: self.odejmowanie())

        self.button0.clicked.connect(lambda: self.wpisz0())
        self.button13.clicked.connect(lambda: self.wpisz13())
        self.button14.clicked.connect(lambda: self.dodawanie())

        self.buttonC.clicked.connect(lambda: self.clearSth())
        self.button15.clicked.connect(lambda: self.wynik())


        # G R I D
        layout.addWidget(self.input, 0, 0, 1, 4)

        layout.addWidget(self.button7, 1, 0)
        layout.addWidget(self.button8, 1, 1)
        layout.addWidget(self.button9, 1, 2)
        layout.addWidget(self.button10, 1, 3)

        layout.addWidget(self.button4, 2, 0)
        layout.addWidget(self.button5, 2, 1)
        layout.addWidget(self.button6, 2, 2)
        layout.addWidget(self.button11, 2, 3)

        layout.addWidget(self.button1, 3, 0)
        layout.addWidget(self.button2, 3, 1)
        layout.addWidget(self.button3, 3, 2)
        layout.addWidget(self.button12, 3, 3)

        layout.addWidget(self.button0, 4, 0)
        layout.addWidget(self.button13, 4, 1)
        layout.addWidget(self.button14, 4, 2, 1, 2)

        layout.addWidget(self.buttonC, 5, 0, 1, 2)
        layout.addWidget(self.button15, 5, 2, 1, 2)


        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


    # D E F S
    def clearSth(self):
        self.input.clear()
        self.enabled()
    def wpisz0(self):
        self.input.insert("0")
        self.enabled()
    def wpisz1(self):
        self.input.insert("1")
        self.enabled()
    def wpisz2(self):
        self.input.insert("2")
        self.enabled()
    def wpisz3(self):
        self.input.insert("3")
        self.enabled()
    def wpisz4(self):
        self.input.insert("4")
        self.enabled()
    def wpisz5(self):
        self.input.insert("5")
        self.enabled()
    def wpisz6(self):
        self.input.insert("6")
        self.enabled()
    def wpisz7(self):
        self.input.insert("7")
        self.enabled()
    def wpisz8(self):
        self.input.insert("8")
        self.enabled()
    def wpisz9(self):
        self.input.insert("9")
        self.enabled()
    def wpisz13(self):
        if (self.input.text() == ''):
            self.input.setText("")
        else:
            self.input.insert(".")
            self.disabled()

    def dodawanie(self):
        if (self.input.text() == ''):
            self.input.setText("")
        else:
            self.input.insert("+")
            self.disabledMinus()
    def odejmowanie(self):
        if (self.input.text() == '-'):
            self.input.setText("")
        else:
            self.input.insert("-")
            self.disabledMinus()
    def mnozenie(self):
        if (self.input.text() == ''):
            self.input.setText("")
        else:
            self.input.insert("*")
            self.disabledMinus()
    def dzielenie(self):
        if (self.input.text() == ''):
            self.input.setText("")
        else:
            self.input.insert("/")
            self.disabledMinus()

    def wynik(self):
        if (self.input.text() == ''):
            self.input.setText("")
        else:
            try:
                haha = eval(self.input.text())
                self.input.setText(str(haha))
            except ZeroDivisionError:
                self.input.setText("")
                print("nie mozna dzielic przez 0")
            else:
                self.input.setText(str(haha))

    def disabled(self):
        self.button10.setDisabled(True)
        self.button11.setDisabled(True)
        self.button12.setDisabled(True)
        self.button13.setDisabled(True)
        self.button14.setDisabled(True)

    def disabledMinus(self):
        self.button10.setDisabled(True)
        self.button11.setDisabled(True)
        self.button13.setDisabled(True)
        self.button14.setDisabled(True)

    def enabled(self):
        self.button10.setDisabled(False)
        self.button11.setDisabled(False)
        self.button12.setDisabled(False)
        self.button13.setDisabled(False)
        self.button14.setDisabled(False)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()