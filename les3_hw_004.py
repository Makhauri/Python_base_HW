def my_func(x, y):
    result = x**y

    return result


def my_func_2(x, y):
    result = 1

    if y > 0:
        while y > 0:
            result *= x
            y -= 1
        return result

    elif y < 0:
        while y < 0:
            result *= x
            y += 1
        return 1 / result


print(my_func(10, -3))
print(my_func_2(10, *3))
