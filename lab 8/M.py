import sys
import psycopg2
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="tododb",
        user="postgres",
        password="123"
    )

def init_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                task_text TEXT NOT NULL,
                is_completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("База данных готова")
    except Exception as e:
        print(f"Ошибка: {e}")

def save_task_to_db(task_text):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (task_text, is_completed)
            VALUES (%s, %s) RETURNING id
        """, (task_text, False))
        task_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return task_id
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return None

def load_tasks_from_db():
    tasks = []
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, task_text, is_completed FROM tasks ORDER BY created_at DESC")
        rows = cursor.fetchall()
        for task_id, task_text, is_completed in rows:
            tasks.append({
                'id': task_id,
                'text': task_text,
                'completed': is_completed
            })
        cursor.close()
        conn.close()
        return tasks
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return []

def update_task_status(task_id, is_completed):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET is_completed = %s WHERE id = %s", (is_completed, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Ошибка обновления: {e}")
        return False

def delete_task_from_db(task_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Ошибка удаления: {e}")
        return False

def get_statistics():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM tasks")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE is_completed = TRUE")
        completed = cursor.fetchone()[0]
        
        incomplete = total - completed
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE DATE(created_at) = CURRENT_DATE")
        today = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        return {
            'total': total,
            'completed': completed,
            'incomplete': incomplete,
            'completion_rate': round(completion_rate, 1),
            'today': today
        }
    except Exception as e:
        print(f"Ошибка получения статистики: {e}")
        return None

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мои задачи")
        self.setGeometry(300, 300, 450, 550)
        
        self.task_ids = {}
        
        init_database()
        
        self.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
            }
            QPushButton {
                background-color: #4a4a4a;
                color: white;
                padding: 8px;
border-radius: 5px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #6a6a6a;
            }
            QPushButton#calcBtn {
                background-color: #2196F3;
            }
            QPushButton#calcBtn:hover {
                background-color: #1976D2;
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
                border: 1px solid #555;
                border-radius: 3px;
            }
        """)
        
        self.pole_vvoda = QLineEdit()
        self.pole_vvoda.setPlaceholderText("Введи задачу...")
        
        self.knopka_dobavit = QPushButton("Добавить")
        self.knopka_dobavit.clicked.connect(self.dobavit_zadachu)
        
        self.spisok = QListWidget()
        
        self.knopka_udalit = QPushButton("Удалить")
        self.knopka_udalit.clicked.connect(self.udalit_zadachu)
        
        self.knopka_vypolnit = QPushButton("Выполнено")
        self.knopka_vypolnit.clicked.connect(self.vypolnit_zadachu)
        
        self.knopka_raschet = QPushButton("Показать расчёты")
        self.knopka_raschet.setObjectName("calcBtn")
        self.knopka_raschet.clicked.connect(self.pokazat_raschety)
        
        layout = QVBoxLayout()
        layout.addWidget(self.pole_vvoda)
        layout.addWidget(self.knopka_dobavit)
        layout.addWidget(self.spisok)
        
        knopki_layout = QHBoxLayout()
        knopki_layout.addWidget(self.knopka_udalit)
        knopki_layout.addWidget(self.knopka_vypolnit)
        
        layout.addLayout(knopki_layout)
        layout.addWidget(self.knopka_raschet)
        
        self.setLayout(layout)
        
        self.zagruzit_zadachi()
    
    def zagruzit_zadachi(self):
        self.spisok.clear()
        self.task_ids.clear()
        
        tasks = load_tasks_from_db()
        for task in tasks:
            self.spisok.addItem(task['text'])
            index = self.spisok.count() - 1
            self.task_ids[index] = task['id']
            
            if task['completed']:
                self.spisok.item(index).setBackground(QColor(76, 175, 80))
    
    def dobavit_zadachu(self):
        text = self.pole_vvoda.text()
        if text:
            task_id = save_task_to_db(text)
            if task_id:
                self.spisok.addItem(text)
                index = self.spisok.count() - 1
                self.task_ids[index] = task_id
                self.pole_vvoda.clear()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось сохранить в БД")
        else:
            QMessageBox.warning(self, "Ошибка", "Поле не может быть пустым")
    
    def udalit_zadachu(self):
        vybrannaya = self.spisok.currentRow()
        if vybrannaya >= 0:
            task_id = self.task_ids.get(vybrannaya)
            if task_id and delete_task_from_db(task_id):
                self.spisok.takeItem(vybrannaya)
                self.obnovit_slovar_id()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось удалить из БД")
        else:
            QMessageBox.warning(self, "Ошибка", "Выбери задачу")
    
    def vypolnit_zadachu(self):
        item = self.spisok.currentItem()
        index = self.spisok.currentRow()
        if item and index >= 0:
            task_id = self.task_ids.get(index)
            if task_id and update_task_status(task_id, True):
                item.setBackground(QColor(76, 175, 80))
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось обновить статус")
        else:
            QMessageBox.warning(self, "Ошибка", "Выбери задачу")
    
    def pokazat_raschety(self):
        stats = get_statistics()
        if stats:
            message = f"""
Статистика задач:

Всего задач:      {stats['total']}
Выполнено:        {stats['completed']}
Осталось:         {stats['incomplete']}
Процент:          {stats['completion_rate']}%
Добавлено сегодня: {stats['today']}
"""
        else:
            message = "Не удалось получить статистику"
        
        QMessageBox.information(self, "Расчёты", message)
    
    def obnovit_slovar_id(self):
        new_task_ids = {}
        for i in range(self.spisok.count()):
            if i in self.task_ids:
                new_task_ids[i] = self.task_ids[i]
        self.task_ids = new_task_ids

if __name__== "__main__":
    app = QApplication(sys.argv)
    okno = TodoApp()
    okno.show()
    sys.exit(app.exec())
    