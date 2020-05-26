class ComplexDigit:
    def __init__(self, real_part, add_part):
        self.__real_part=real_part
        self.__add_part=add_part

    def __add__(self, other):
        return ComplexDigit(self.__real_part+ other.__real_part, self.__add_part+other.__add_part)

    def __mul__(self, other):
        return ComplexDigit(self.__real_part*other.__real_part-self.__add_part*other.__add_part, self.__real_part*other.__add_part+self.__add_part*other.__real_part)

    def __str__(self):
        return f'{str(self.__real_part)}+{str(self.__add_part)}*i'

a=ComplexDigit(1, -1)
b=ComplexDigit(3, 6)
print(f'a+b={a+b}')
print(f'a*b={a*b}')


