class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return '{0} {1}'.format(self.name, self.surname)

    def get_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position('John', 'Devidson', 'engineer', 50000, 15000)
print(position.name)
print(position.surname)
print(position._income)
print(position.get_full_name())
print(position.get_income())