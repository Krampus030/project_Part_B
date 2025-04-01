import sqlite3


class InfoDatabase:
    """
    Database for customer seat and personal information.
    """

    def __init__(self):
        self.conn = sqlite3.connect("info.db")
        self.cursor = self.conn.cursor()
        self.create_customer_table()
        self.create_info_table()


    def create_customer_table(self):
        """
        Create seat booking table if it doesn't exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        reference TEXT NOT NULL,
        seat TEXT NOT NULL
        )
        ''')
        self.conn.commit()


    def create_info_table(self):
        """
        Create customer info table if it doesn't exist.
        """
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
        """
        Insert a new customer record into the database.
        """
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


    def insert_customer_booking(self, name, reference, seat):
        try:
            self.cursor.execute('''
                INSERT INTO customer (name, reference, seat)
                VALUES (?, ?, ?)
            ''', (name, reference, seat))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error inserting booking into customer table:", e)
            return False


    def delete_customer_info(self, name, gender, phone, passport):
        """
        Delete a customer record by matching all fields.
        """
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


    def delete_customer_booking(self, name):
        """
        Delete customer's booking from customer table and return released seat.
        """
        self.cursor.execute('''
            SELECT seat FROM customer WHERE name=?
        ''', (name,))
        result = self.cursor.fetchone()

        if result:
            seat = result[0]
            self.cursor.execute('''
                DELETE FROM customer WHERE name=?
            ''', (name,))
            self.conn.commit()
            return seat
        else:
            return None


    def fetch_all_customer_info(self):
        """
        Return all records from customer_info table.
        """
        self.cursor.execute("SELECT * FROM customer_info")
        return self.cursor.fetchall()


    def get_all_references(self):
        """
        Return all reference from customer table
        """
        self.cursor.execute("SELECT reference FROM customer")
        results = self.cursor.fetchall()
        return {row[0] for row in results}


    def get_all_customer(self):
        """
        Return name and contact info for all bookings.
        """
        self.cursor.execute("SELECT name, gender, phone_number, passport_number FROM customer_info")
        return self.cursor.fetchall()


    def get_all_bookings(self):
        """
        Return id and reference of customer for all bookings.
        """
        self.cursor.execute("SELECT id, name, reference, seat FROM customer")
        return self.cursor.fetchall()


database = InfoDatabase()
print(database.get_all_bookings())
