full_string = input('Введите слова разделенные пробелом:')
#full_string = 'копыто ферма молокобрабатывающий'
i=1
for value in full_string.split():
    print(f'{i}: {value[0:10]}')
    i = i + 1
