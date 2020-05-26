class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyDivision:

    @staticmethod
    def div(a,b):
        if b==0: raise MyZeroDivisionError('Ошибка: нельзя делить на ноль!')
        return a/b

try:
    a, b  = map(int,(input('введите два чила через пробел:').split()))
    print (f'a/b={MyDivision.div(a, b)}')
except MyZeroDivisionError as ex:
    print(ex)