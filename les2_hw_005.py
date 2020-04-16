my_list = [7, 5, 3, 3, 2]

print(my_list)

user_num = input('Введите новое число: ')

for ind, val in enumerate(my_list):
    if int(user_num) == val:
        my_list.insert(ind+1, val)
        break
    elif int(user_num) > val:
        my_list.insert(ind, int(user_num))
        break
    elif int(user_num)+1 == val:
        my_list.insert(ind+1, int(user_num))
        break

print(my_list)

