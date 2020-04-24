"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее."""

from itertools import cycle, count

my_list = [2, 4, 5, 6, 7, 8, 9]

сount = 0
for i in cycle(my_list):
    if сount > 50:
        break
    print(i)
    сount += 1


for i in count(50):
    if i > 15:
        break
    else:
        print(i)
