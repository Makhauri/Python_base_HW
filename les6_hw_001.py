import time
from itertools import cycle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        """
        Эта функция принимает список цветов и выводит их значение циклично, с разной
        задержкой для кадого
        :return: None
        """
        i = 0
        for c in cycle(self.__color):
            if i > 10:
                break
            print(c)
            if c == 'red':
                time.sleep(1)
            elif c == 'yellow':
                time.sleep(2)
            elif c == 'green':
                time.sleep(4)
            i += 1


x = TrafficLight()
x.running()
