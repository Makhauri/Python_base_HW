def sum_funk_1(*args):
    num = 0

    for i in args:
        num += int(i) if i else 0
    return num


my_num = 0

while True:
    user_nums = input('Введите строку чисел раздеоенных пробелом: ').split(' ')

    my_num += sum_funk_1(*user_nums)


    print(my_num)
