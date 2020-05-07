def my_pow_short(x: float, y: int):
    return x ** y


def my_pow_long(x: float, y: int):
    if y >= 0: pass #вообще можно так не длать функционал возведения в степень будет работать
    pow_x = x
    for i in list(range(1, abs(y))):
        pow_x = pow_x * x
    return 1 / pow_x

try:
    x = float(input('ведите натуральное положительное число Х:'))
    y = int(input('ведите целое отрицательное число Y:'))
    if x < 0 or y >= 0:
        raise ValueError
    #x = 2
    #y = -3
    print(my_pow_short(x, y))
    print(my_pow_long(x, -y))
    # вишенка на торте
    my_pow_lambda = lambda var1, var2: var1 ** var2
    print(my_pow_lambda(x, y))
except ValueError:
    print('Вы вводите некорректные значения')
