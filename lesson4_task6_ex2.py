from sys import argv
from itertools import cycle


def int_cicle(list):
    for cur_num in cycle(list):
        yield cur_num


try:
    src_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    max_retry = argv[1]
    cur_retry = 1
    for i in int_cicle(src_list):
        print(i)
        cur_retry += 1
        if cur_retry > int(max_retry):
            break
except ValueError:
    print('Вы передали некорректные значения')