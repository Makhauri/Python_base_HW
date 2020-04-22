def my_funс(x: int, y: int):
    """
    Эта функция принимает 2 числа и выводит
    результат деления первого числа на второе
    :param x: int
    :param y: int
    :return: None
    """
    if not x % y:
        result = x // y
    else:
        result = x / y
    print(f'Результат деления {x} на {y}: {round(result, 2)}')


my_list = []

for i in range(2):

    user_num = input('Введите два одно число: ')

    if int(user_num) <= 0:
        print('Ошибка. Введите числа больше нуля')
        continue

    if user_num.isdigit():
        user_num = int(user_num)

    my_list.append(user_num)

my_funс(my_list[0], my_list[1])
