import sqlite3

# from classes import Document

class Database(object):
    # потом надо засунуть в YAML с ограничением по доступу
    __DB_LOCATION = "IncomingDocuments.db"

    def __init__(self, db_location=None):
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def __enter__(self):
        """could be used with 'with'"""
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        """could be used with 'with'"""
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def __del__(self):
        self.connection.close()

    def close(self):
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)
        # if new_data.lstrip().upper().startswith("SELECT"):
        #     return self.cur.fetchall()

    def insert_doc(self, new_data):
        """add one document to database"""
        self.create_table()
        self.cur.execute('INSERT INTO documents(date, number, name, source) VALUES(?, ?, ?, ?)', new_data)

    def executemany(self, many_new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.executemany('INSERT INTO documents(date, number, name, source) VALUES(?, ?, ?, ?)', many_new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS documents (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL DEFAULT '2021.01.01',
            number TEXT NOT NULL DEFAULT '',
            name TEXT NOT NULL DEFAULT 'letter',
            source TEXT
            );
            ''')

    def commit(self):
        self.connection.commit()
