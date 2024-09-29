import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()


def create_table():
    c.execute(
        '''
         CREATE TABLE IF NOT EXISTS expenses(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         date TEXT,
         description TEXT,
         category TEXT,
         amt REAL
         )
         '''
    )
    conn.commit()


def add_expenses(name, date, description, category, amt):
    c.execute(
        '''
      INSERT INTO expenses(name,date,description,category,amt)
      VALUES (?,?,?,?,?)
      ''', (name, date, description, category, amt)
    )
    conn.commit()


def show_expenses(name):
    c.execute(
        '''
        SELECT * FROM expenses WHERE name = ?
        ''', (name,)
    )
    data = c.fetchall()
    return data


def view_expenses_name(name):
    c.execute(
        '''
        SELECT category, SUM(amt)
        FROM expenses
        WHERE name = ?
        GROUP BY category
        ''', (name,)
    )
    data = c.fetchall()
    return data
