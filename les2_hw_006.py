#my_list = [
 #   (1, {'название': 'Компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
  #  (2, {'название': 'Принтер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
   # (3, {'название': 'Сканер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#]

#my_dict = {}

#for turp in my_list:
    #for dicti in turp:
    #    print(dicti)

num = 1
while num < 5:
    var = 'название'
    var_02 = 'цена'
    val_01 = input('Введите название товара: ')
    val_02 = input('Введите цену товара: ')


    my_list = []
    dict_name = {}
    dict_price = {}
    my_turple = (num, dict_name,)



    dict_name.update({var: val_01})

    my_list.append(my_turple)


    num += 1

print(my_list)







