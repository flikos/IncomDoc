import datetime

class Document:
    def __init__(self, date, number, source):
        self.incoming_date = date
        self.incomming_number = number
        self.source = source
        self.executor = None
        self.term_date = None
    
    def __str__(self):
        text = 'Документ № {} от {}'.format(self.incomming_number, self.incoming_date)
        if self.term_date:
            text += ' срок исполнения: {}'.format(self.term_date)
        if self.executor:
            text += ' исполнитель: {}'.format(self.executor)
        return text

    def setExecutor(self, executor):
        if isinstance(executor, Executor):
            self.executor = executor

    def setTerm(self, date):
        self.term_date = date


class Agent:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Контрагент: {}'.format(self.name)


class Employer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Сотрудник - {}'.format(self.name)

class Executor(Employer):
    pass

if __name__ == '__main__':
    doc = Document('25.02.2021', 1, 'opfr')
    print(doc)

    agent = Agent('opfr')
    print(agent)

    mag = Executor('mag')
    print(mag)

    doc.setExecutor(mag)
    doc.setTerm('28.02.2021')
    print(doc)

    def get_datetime_str():
        return datetime.datetime.today().strftime('%Y.%m.%d sec: %S')
    print(get_datetime_str())
    print(get_datetime_str(s))

