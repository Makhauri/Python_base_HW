class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass: int, thick: int) -> None:
        """
        Этф функция принимает на вход два параметра - массу асфальта и толщину полотна
        и выводит результат вычисления - длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
        толщиной в 1 см*число см толщины полотна.

        :param mass: int
        :param thick: int
        :return:
        """
        result = self._length * self._width * mass * thick
        print(f'{self._length}м * {self._width}m * {mass}кг * {thick}cm = {round(result * 0.001)}т')


x = Road(20, 5000)
x.mass(25, 5)