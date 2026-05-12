import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мои задачи")
        self.setGeometry(300, 300, 400, 500)
        
        # Стилизация
        self.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
            }
            QPushButton {
                background-color: #4a4a4a;
                color: white;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #6a6a6a;
            }
            QListWidget {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #555;
            }
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                padding: 5px;
            }
        """)
        
        # Виджеты
        self.pole_vvoda = QLineEdit()
        self.pole_vvoda.setPlaceholderText("Введи задачу...")
        
        self.knopka_dobavit = QPushButton("➕ Добавить")
        self.knopka_dobavit.clicked.connect(self.dobavit_zadachu)
        
        self.spisok = QListWidget()
        
        self.knopka_udalit = QPushButton("❌ Удалить")
        self.knopka_udalit.clicked.connect(self.udalit_zadachu)
        
        self.knopka_vypolnit = QPushButton("✅ Выполнено")
        self.knopka_vypolnit.clicked.connect(self.vypolnit_zadachu)
        
        # Компоновка
        layout = QVBoxLayout()
        layout.addWidget(self.pole_vvoda)
        layout.addWidget(self.knopka_dobavit)
        layout.addWidget(self.spisok)
        
        knopki_layout = QHBoxLayout()
        knopki_layout.addWidget(self.knopka_udalit)
        knopki_layout.addWidget(self.knopka_vypolnit)
        
        layout.addLayout(knopki_layout)
        self.setLayout(layout)
    
    def dobavit_zadachu(self):
        text = self.pole_vvoda.text()
        if text:
            self.spisok.addItem(text)
            self.pole_vvoda.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Поле не может быть пустым!")
    
    def udalit_zadachu(self):
        vybrannaya = self.spisok.currentRow()
        if vybrannaya >= 0:
            self.spisok.takeItem(vybrannaya)
        else:
            QMessageBox.warning(self, "Ошибка", "Выбери задачу для удаления!")
    
    def vypolnit_zadachu(self):
        item = self.spisok.currentItem()
        if item:
            # Просто делаем задачу зелёной
            item.setBackground(QColor(76, 175, 80))  # ярко-зелёный
            # Можно добавить зелёный текст (по желанию)
            # item.setForeground(QColor(255, 255, 255))
        else:
            QMessageBox.warning(self, "Ошибка", "Выбери задачу!")

app = QApplication(sys.argv)
okno = TodoApp()
okno.show()
sys.exit(app.exec())