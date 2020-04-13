#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_num = input('Введите целое положительное число')

if int(user_num) <= 0:
    print('Ошибка! Вы должны ввести положительное чиисло')
else:
    result = '0'
    i = 0
    while i < len(user_num):
        if int(user_num[i]) > int(result):
            result = user_num[i]
            i += 1
        else:
            i += 1


print(result)

