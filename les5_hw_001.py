while True:
    user_data = input("Введите данные")
    if not user_data:
        break
    else:
        with open('les5_hw_data_001.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{user_data}\n')
