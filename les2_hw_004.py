my_list = [7, 5, 3, 3, 2]

user_num = input('Введите несколько слов: ')

for i, t in enumerate(user_num.split()):
    if len(t) < 10:
        print(i, t)
    else:
        print(i, t[:10])