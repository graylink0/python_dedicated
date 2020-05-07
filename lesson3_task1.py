def my_div(a: int, b: int) ->float:
    """реализуем деление A/B
    :param
    a - делимое
    b - делитель"""
    try:
        return a/b
    except ZeroDivisionError:
        print('Ошибка: Вы передали в качестве делителя ноль!')

try:
    a = int(input ('Введите делимое:'))
    b = int(input('Введите делитель:'))
    c = my_div(a, b)
    print (f'результат деления {a}/{b}={c:.2f}')
except ValueError:
    print('Вы вводите некорректные значения')

