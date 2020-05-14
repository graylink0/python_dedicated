import re

try:
    file = open(r'c:\temp\example\text_6.txt', mode='r', encoding='utf-8')
    final_dict = {}
    for line in file:
        discipine = line.split(':')[0]
        hours = map(int, re.findall(r'[0-9]+', line))
        hours_sum = sum(hours)
        final_dict.update({discipine: hours_sum})
except IOError:
    print('Ошибка ввода/вывода')
finally:
    file.close()
    print(final_dict)
