#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_num = input('Введите число: ')


sum_var = int(user_num) + int(user_num + user_num) + int(user_num + user_num + user_num)

print(sum_var)

