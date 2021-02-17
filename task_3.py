class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        """ получение полного имени сотрудника
         :return: str
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """получение дохода с учетом премии
         :return:str
        """
        return f'{self._income.get("wage") + self._income.get("bonus")}'


position_1 = Position('Иван', 'Иванов', 'младший менеджер', 20000, 5000)
print(position_1.get_full_name())
print(position_1.get_total_income())
print(f"{position_1.__dict__} '_income':{position_1._income}")

position_2 = Position('Олег', 'Андреев', 'старший менеджер', 30000, 10000)
print(position_2.get_full_name())
print(position_2.get_total_income())
print(f"{position_2.__dict__} '_income':{position_2._income}")