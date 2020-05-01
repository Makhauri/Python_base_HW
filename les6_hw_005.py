class Stationery:
    title = ''

    def draw(self):
        """
        Эта функция выводит сообщение
        :return: None
        """
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'ручка'

    def draw(self):
        """
        Эта функция выводит уникальное сообщение
        :return:
        """
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'карандаш'

    def draw(self):
        """
        Эта функция выводит уникальное сообщение
        :return:
        """
        print('Запуск отрисовки карандашем')


class Handle(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'маркер'

    def draw(self):
        """
        Эта функция выводит уникальное сообщение
        :return:
        """
        print('Запуск отрисовки маркером')


stat_01 = Pen()
stat_02 = Pencil()
stat_03 = Handle()

print(stat_01.title)
print(stat_02.title)
print(stat_03.title)

stat_01.draw()
stat_02.draw()
stat_03.draw()
