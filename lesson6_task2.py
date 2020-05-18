class Road:
    def __init__(self, lenght: int, width: int):
        """
        Дорога
        :param lenght:  длинна дороги в метрах
        :param width: ширина дороги в метрах
        """
        self._lenght = lenght
        self._width = width
        self._mass_one_sm = 25
        self._depth=5
    def calculate_totall_mass(self):
        """
        посчитать массу асфальта для дороги
        :return: масса асфальта в тоннах
        """
        totall_mass = self._lenght * self._width * self._mass_one_sm * self._depth
        return totall_mass/1000  #тонны. Если убдет время сделать метод нормализации

#lenght = int(input('Введите длинну дороги в метрах:'))
#width = int(input('Введите ширину дороги в метрах:')
lenght = 20
width = 5000
road=Road(20 , 5000)
print (f'масса асфальта: {road.calculate_totall_mass()} тонн')
