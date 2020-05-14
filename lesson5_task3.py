def get_emloy_list(file):
    try:
        emloylist = []
        for line in file:
            list = line.split()
            emloylist.append({'name': list[0], 'pay': float(list[1])})
    except IOError:
        print('Ошибка ввода/вывода!')
    finally:
        file.close()
        return emloylist
def get_slaves(list_eml):
    for employ in list_eml:
        if employ.get('pay') < 20000:
            yield employ.get('name')
def get_average_pay(list_eml):
    sum_pay = 0.0
    for employ in list_eml:
        sum_pay = sum_pay+employ.get('pay')
    return sum_pay/len(list_eml)



file = open(r'c:\temp\example\text_3.txt', encoding='utf-8')
list_emloy=get_emloy_list(file)
print(f"Следующие сотрудники получают меньше 20000:")
for name in get_slaves(list_emloy):
    print(f"{name}")
print(f'Средний размер оплаты труда: {get_average_pay(list_emloy)}')
