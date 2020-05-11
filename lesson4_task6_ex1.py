from sys import argv
from itertools import count

def int_generator(num):
    for cur_num in count(num):
        yield cur_num


try:
    num, max_retry = argv[1:]
    cur_retry=1
    for i in int_generator(int(num)):
        print(i)
        cur_retry += 1
        if cur_retry > int(max_retry):
            break
except ValueError:
    print('Вы передали некорректные значения')
