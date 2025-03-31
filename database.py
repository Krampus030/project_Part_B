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

    def insert_customer_info(self, name, gender, phone, passport):
        try:
            self.cursor.execute('''
                    INSERT INTO customer_info (name, gender, phone_number, passport_number)
                    VALUES (?, ?, ?, ?)
                ''', (name, gender, phone, passport))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error inserting into database:", e)
            return False

    def delete_customer_info(self, name, gender, phone, passport):
        self.cursor.execute('''
            SELECT rowid FROM customer_info
            WHERE name=? AND gender=? AND phone_number=? AND passport_number=?
        ''', (name, gender, phone, passport))
        result = self.cursor.fetchone()

        if result:
            self.cursor.execute('''
                DELETE FROM customer_info
                WHERE name=? AND gender=? AND phone_number=? AND passport_number=?
            ''', (name, gender, phone, passport))
            self.conn.commit()
            return True
        else:
            return False

    def fetch_all_customer_info(self):
        self.cursor.execute("SELECT * FROM customer_info")
        return self.cursor.fetchall()



database = InfoDatabase()
print(database.fetch_all_customer_info())
