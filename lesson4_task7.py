from sys import argv

def my_factorial(num):
    cur_factorial=1
    for cur_num in range(1, num+1):
        cur_factorial = cur_factorial*cur_num
        yield cur_factorial


try:
    num, max_retry = argv[1:]
    cur_retry = 1
    for i in my_factorial(int(num)):
        print(i)
        cur_retry += 1
        if cur_retry > int(max_retry):
            break
except ValueError:
    print('Вы передали некорректные значения')