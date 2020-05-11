from functools import reduce
def my_mul(a, b):
    return a*b

list=[el for el in range(100,1001) if el%2==0]
print(reduce(my_mul, list))
#чета много