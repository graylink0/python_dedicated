var=int(input('Введите простое число:'))
max=0
while var >= 1 :
    cur_val=var % 10
    if cur_val > max:
        max=cur_val
    var=var//10
print(f'самое большое: {max}')