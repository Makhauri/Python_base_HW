# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [1, 10, 12, 456, -7, 8, 10]

result = []

for i, itm in enumerate(my_list):
    if i and itm > my_list[i - 1]:
        result.append(itm)

print(result)

result_02 = [itm for i, itm in enumerate(my_list) if i and itm > my_list[i-1]]

print(result_02)