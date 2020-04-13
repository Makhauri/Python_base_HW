#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Введите время в секундах: '))


time_in_sec = user_time % 60
time_in_min = (user_time // 60) % 60
time_in_hour = user_time // 3600

if time_in_sec < 10:
    time_in_sec = '0' + str(time_in_sec)
if time_in_min < 10:
    time_in_min = '0' + str(time_in_min)
if time_in_hour < 10:
    time_in_hour = '0' + str(time_in_hour)

print(f'{time_in_hour}:{time_in_min}:{time_in_sec}')

