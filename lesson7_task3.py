class Cell:
    def __init__(self, units: int):
        self.units = units

    def __add__(self, other):
        return self.units+other.units

    def __sub__(self, other):
        if self.units>= other.units:
            return self.units - other.units
        else:
            raise Exception('Ошибка: во вторй клетке больше ячеек!')
    def __mul__(self, other):
        return self.units * other.units

    def __truediv__(self, other):
        return self.units // other.units

    def make_order(cell, count:int):
        celoe=cell.units//count
        ostatok=cell.units%count
        result = ''
        gen_list=[('*'*count+'\n') for i in range(0,celoe)]
        for chars in gen_list:
            result+=chars
        result+='*'*ostatok+'\n'
        return result


c1=Cell(6)
c2=Cell(2)
print(f'c1+c2: {c1+c2}')
print(f'c1-c2: {c1-c2}')
try:
    print(f'c2-c1: {c2-c1}')
except:
    print ('словил ошибку')
print(f'c1*c2: {c1*c2}')
print(f'c1/2: {c1/c2}')
print(Cell.make_order(Cell(12), 4))