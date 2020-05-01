class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        '''
        Эта функция складывает переменную имени и фамилии и возвращает полное имя
        :return: str
        '''
        return self.name + ' ' + self.surname

    def get_total_income(self):
        '''
        эта функция возвращает сумму 1 и 2 значений словаря
        :return: int
        '''
        return self._income['wage'] + self._income['bonus']


inc = {'wage': 1300, 'bonus': 500}
char_01 = Position('Иван', 'Иванов', 'Директор', inc)

print(char_01.get_full_name())
print(char_01.get_total_income())
