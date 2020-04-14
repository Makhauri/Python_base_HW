my_list = []
count = 7
i = 0


while i < count:
    val = input('Введите любое значение: ')
    my_list.append(val)
    i += 1

print(f'Данный список - {my_list}')


t = 0

while t < len(my_list):
    if not t % 2:
        if my_list[t] != my_list[-1]:
            temp_var = my_list[t]
            my_list[t] = my_list[t+1]
        else:
            t += 1
            continue

    else:
        my_list[t] = temp_var

    t += 1

print(f'Измененный список - {my_list}')

