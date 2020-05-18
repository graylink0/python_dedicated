class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        #Не уверен что со словарем именно это имелось в виду, но другого не придумал
        self._name = name
        self._surname = surname
        self._position = position
        self._income = income


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self._name } {self._surname}'

    def get_total_income(self):
        return self._income.get('wage')+self._income.get('bonus')


ivan = Position('Иван', 'Иванов', 'инженер', {'wage': 30000, 'bonus': 5000})
moisey = Position('Моисей', 'Исаакович', 'главный бухгалтер', {'wage': 8000000000, 'bonus': 5300000000})
print(f'{ivan.get_full_name()} получает {ivan.get_total_income()}')
print(f'{moisey.get_full_name()} получает {moisey.get_total_income()}')
