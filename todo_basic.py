# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: To Do Basic
# Version: 1.0: Base version by author
import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def enter_name(self):
        while True:
            input_name = input('>>> Enter Task Name: ').strip()
            if input_name == '':
                print('Info: Received an Empty String. Task Name cannot be empty.')
                continue
            if self.find_task(input_name) is not None:
                print('You have entered an existing name. Please Retry with different name.')
                continue
            return input_name

    @staticmethod
    def enter_priority():
        while True:
            try:
                input_priority = int(input('>>> Enter Priority: ').strip())
            except ValueError:
                print('Entered data is not an Integer. Please re-try.')
                continue
            if input_priority < 1:
                print('Priority should not be less than 1. Please re-try.')
                continue
            return input_priority

    def add_task(self):
        name = self.enter_name()
        priority = self.enter_priority()
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def find_task(self, name):
        self.c.execute('SELECT * FROM tasks WHERE name = ?', (name,))
        data = self.c.fetchone()
        if data is None:
            return None
        return data

    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        rows = self.c.fetchall()
        for row in rows:
            print(row)


app = Todo()
app.add_task()
app.find_task('Sample 1')
app.show_tasks()
