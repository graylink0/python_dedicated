def my_func(a: int, b: int, c: int):
    """выберем сумму двух наибольших аргументов"""
    list_vars = [a, b, c]
    list_vars.sort()
    return list_vars[-2]+list_vars[-1]


try:
    a = int(input('Введите целое число:'))
    b = int(input('еще одно:'))
    c = int(input('последнее:'))
    print(my_func(a, b, c))
except ValueError:\
    print('Вы вводите некорректные значения')