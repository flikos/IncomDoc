import datetime
import sqlite3 as sl

# временное решение для удобного отслеживания аттрибутов
from classtools import AttrDisplay


class Document(AttrDisplay):
    def __init__(self, date, number, name, source=None):
        self.date = date
        self.number = number
        self.name = None or name
        self.source = None or source

class Contractor:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Контрагент: {}'.format(self.name)


class Executor:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Сотрудник - {}'.format(self.name)


# ======== тестирование ========
if __name__ == '__main__':
    def get_today_str():
        return datetime.datetime.today().strftime('%Y.%m.%d')


    doc = Document(get_today_str(), 1, 'Письмо', 'opfr')
    print(doc)

    # подключаемся к базе
    con = sl.connect('IncomingDocuments.db')
    RESTARTDB = 0
    if RESTARTDB:
        # удаляем базу
        with con:
            con.execute("""
            DROP TABLE IF EXISTS documents
            """)
    # создаем базу
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS documents (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL DEFAULT '2021.01.01',
            number TEXT NOT NULL DEFAULT '',
            name TEXT NOT NULL DEFAULT 'letter',
            source TEXT
            );
        """)
    # вносим данные
    sql = 'INSERT INTO documents (date, number, name, source) values(?, ?, ?, ?)'
    data = [
        (get_today_str(), '100', 'letter', 'opfr'),
        (get_today_str(), '101', 'query  ', 'adm'),
        (get_today_str(), '102', 'query', 'opfr')
    ]
    with con:
        # pass
        con.executemany(sql, data)
    # делаем выборку
    with con:
        data = con.execute("SELECT * FROM documents WHERE name = 'query'")
    # печатаем полученные данные
    for row in data:
        print(row)
    
    con.close