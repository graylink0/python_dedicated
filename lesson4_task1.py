from sys import argv

try:
    work_hours, cost_hour, primary_pay = argv[1:4]
    sum_charge = (int(work_hours)*float(cost_hour))+float(primary_pay)
    print(f'Заработная плата работника: {sum_charge}')
except ValueError:
    print('Вы передали некорректные значения')
