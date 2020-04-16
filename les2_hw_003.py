#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# Решение через list

months_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

user_num = input('Введите номер месяца: ')

for i in range(len(months_list)):
    if int(user_num) in months_list[0:3]:
        print('Это зима')
        break
    elif int(user_num) in months_list[3:6]:
        print('Это весна')
        break
    elif int(user_num) in months_list[6:9]:
        print('Это лето')
        break
    elif int(user_num) in months_list[9:12]:
        print('Это осень')
        break

# Решение через dict

month_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 4, 8], 'осень': [9, 10, 11]}

for k, v in month_dict.items():
    if int(user_num) in v:
        print(f"Это {k}")
