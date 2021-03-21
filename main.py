import classes
import datetime
import random
import incomming_documens_db_operarions as DB


if __name__ == '__main__':

    def get_today_str():
        return datetime.datetime.today().strftime('%Y.%m.%d')

    with DB.Database('IncomingDocuments.db') as db:
        db.execute('SELECT * FROM documents WHERE name ="query" AND source="opfr"')
        for row in db.cur:
            print(row)


    doc1 = classes.Document(get_today_str(), str(random.randint(1, 200)), 'Настройка XML-менеджера', 'opfr')
    with DB.Database('IncomingDocuments.db') as db:
        db.insert_doc(doc1.aslist())
        db.execute('SELECT * FROM documents')
        for row in db.cur:
            print(row)

    