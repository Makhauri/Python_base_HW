

a_var = input('Введите результат первого дня: ')
b_var = input('Введите общий результат который вы ищите: ')
day = 1

if a_var.isdigit() and b_var.isdigit():
    a_var = int(a_var)
    b_var = int(b_var)

while True:

    print(f'{day}-й день: {round(a_var,2)}')

    if a_var >= b_var:

        print(f'На {day}-й день спортсмен достиг результата - не менее {round(a_var,2)} км')
        break

    a_var += a_var * 0.1
    day += 1

