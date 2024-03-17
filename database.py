import sqlite3

conn = sqlite3.connect('company.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
                    employee_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    salary INTEGER NOT NULL,
                    position TEXT NOT NULL
                )''')
