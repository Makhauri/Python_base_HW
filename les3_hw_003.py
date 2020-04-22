def my_func2(x: int, y: int, z: int) -> int:
    """
        Эта функция принимает 3 числа и возвращает
        результат сложения двух наибольших
        :param x: int
        :param y: int
        :param y: int
        :return: int

    """
    my_list = [x, y, z]
    my_list.sort()
    return my_list[-1] + my_list[1]


print(my_func2(2, 4, 5))

