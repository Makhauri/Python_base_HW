class Car:

    def __init__(self, speed=0, color='red', name='nissan', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """
        Эта функция  выводит сообщение о том что машина поехала
        :return: None
        """
        print('Машина поехала')

    def stop(self):
        """
        Эта функция выводит сообщение о том что машина остановилась
        :return: None
        """
        print('Машина остановилась')

    def turn(self, direction):
        """
        Эта функция выводит сообщение о том что пашина поехала направо, если атрибут direction(r)
        И поехала налево, если direction(l)
        :return: None
        """
        if direction == 'r':
            print('Машина поехала направо')
        elif direction == 'l':
            print('Машина поехала налево')

    def show_speed(self):
        """
        Этп функция выводит значения атрибута speed
        :return: None
        """
        print(self.speed)


class TownCar(Car):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        """
        Эта функция выводит сообщение о том, что скорость  превышена, если значение атрибута speed
        больше 40, если меньше, то выводится значение атрибута speed
        :return: None
        """
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(self.speed)

class WorkCar(Car):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        """
        Эта функция выводит сообщение о том, что скорость  превышена, если значение атрибута speed
        больше 60, если меньше, то выводится значение атрибута speed
        :return: None
        """
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_police = True


class SportCar(Car):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)


car = Car()
car2 = TownCar(45, 'красный', 'тойота')
car3 = WorkCar(65, 'зеленый', 'шевроле')
car4 = PoliceCar(90, 'синий', 'мерседес')
car5 = SportCar(140, 'белый', 'рено')


car.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()
car5.show_speed()

print(car4.is_police)