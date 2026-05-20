import sys
import typer
from PySide6.QtWidgets import *
from lab_package import lab4, lab5, lab6

app = typer.Typer()

# ============= GUI =============
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабы 4-6")
        self.setGeometry(300, 200, 500, 450)
        tabs = QTabWidget()
        self.setCentralWidget(tabs)
        
        # Лаба 4
        t4 = QWidget()
        tabs.addTab(t4, "Лаба 4")
        l = QVBoxLayout(t4)
        l.addWidget(QLabel("Список:"))
        self.inp4 = QTextEdit()
        self.inp4.setText("[1,2,[3,4]]")
        l.addWidget(self.inp4)
        b = QPushButton("Считать")
        b.clicked.connect(self.lab4)
        l.addWidget(b)
        self.res4 = QLabel("0")
        l.addWidget(self.res4)
        
        # Лаба 5
        t5 = QWidget()
        tabs.addTab(t5, "Лаба 5")
        l = QVBoxLayout(t5)
        l.addWidget(QLabel("Операция:"))
        self.op5 = QComboBox()
        self.op5.addItems(['+','-','*','/'])
        l.addWidget(self.op5)
        l.addWidget(QLabel("Нач.значение:"))
        self.init5 = QLineEdit("1")
        l.addWidget(self.init5)
        l.addWidget(QLabel("Число:"))
        self.x5 = QLineEdit("2")
        l.addWidget(self.x5)
        l.addWidget(QLabel("Повторов:"))
        self.rep5 = QLineEdit("1")
        l.addWidget(self.rep5)
        b = QPushButton("Вычислить")
        b.clicked.connect(self.lab5)
        l.addWidget(b)
        self.res5 = QLabel("")
        l.addWidget(self.res5)
        
        # Лаба 6
        t6 = QWidget()
        tabs.addTab(t6, "Лаба 6")
        l = QVBoxLayout(t6)
        l.addWidget(QLabel("Кол-во:"))
        self.cnt6 = QSpinBox()
        self.cnt6.setRange(1,50)
        self.cnt6.setValue(5)
        l.addWidget(self.cnt6)
        l.addWidget(QLabel("Min/Max:"))
        h = QHBoxLayout()
        self.min6 = QLineEdit("1")
        self.max6 = QLineEdit("67")
        h.addWidget(self.min6)
        h.addWidget(QLabel("-"))
        h.addWidget(self.max6)
        l.addLayout(h)
        l.addWidget(QLabel("Seed:"))
        self.seed6 = QLineEdit()
        l.addWidget(self.seed6)
        b = QPushButton("Сгенерировать")
        b.clicked.connect(self.lab6)
        l.addWidget(b)
        self.res6 = QLabel("")
        l.addWidget(self.res6)
        l.addStretch()
    
    def lab4(self):
        try:
            self.res4.setText(str(lab4.recursive(eval(self.inp4.toPlainText()))))
        except:
            self.res4.setText("Ошибка")
    
    def lab5(self):
        try:
            calc = lab5.make_calc(self.op5.currentText(), float(self.init5.text()))
            n = int(self.rep5.text())
            if n > 1:
                @lab5.repeat_decorator(n)
                def f(x):
                    return calc(x)
                self.res5.setText(str(f(float(self.x5.text()))))
            else:
                self.res5.setText(str(calc(float(self.x5.text()))))
        except:
            self.res5.setText("Ошибка")
    
    def lab6(self):
        try:
            if self.seed6.text():
                lab6.init_rng(int(self.seed6.text()))
            self.res6.setText(str(lab6.generate(self.cnt6.value(), int(self.min6.text()), int(self.max6.text()))))
        except:
            self.res6.setText("Ошибка")

# ============= CLI =============
@app.command()
def lab4(lst: str):
    print(lab4.recursive(eval(lst)))

@app.command()
def lab5(op: str, x: float, init: float = 1, rep: int = 1):
    calc = lab5.make_calc(op, init)
    if rep > 1:
        @lab5.repeat_decorator(rep)
        def f(v):
            return calc(v)
        print(f(x))
    else:
        print(calc(x))

@app.command()
def lab6(cnt: int = 5, mn: int = 1, mx: int = 67, sd: int = None):
    if sd:
        lab6.init_rng(sd)
    print(lab6.generate(cnt, mn, mx))

@app.command()
def gui():
    q = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(q.exec())

if __name__ == "__main__":
    app()