month_num = input('Введите номер месяца:')
if month_num.isdigit()==False:
    print("вы ввели не цифру")
    exit(1)
month_num = int(month_num)
if month_num in range(1, 13):
    period_year = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
    period_index = month_num//3
    print(f'Этот месяц относится к периоду: {period_year.get(period_index)}')
else:
    print('Неправильный номер мясца')
    exit
