import sqlite3


class InfoDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("info.db")
        self.cursor = self.conn.cursor()
        self.create_customer_table()
        self.create_info_table()

    def create_customer_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        seat TEXT NOT NULL
        )
    ''')
        self.conn.commit()

    def create_info_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_info(
        name TEXT NOT NULL,
        gender TEXT NOT NULL,
        phone_number INTEGER NOT NULL,
        passport_number TEXT NOT NULL
        )
    ''')
        self.conn.commit()


database = InfoDatabase()
