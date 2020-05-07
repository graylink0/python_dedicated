list_var = []
is_continue = True
while is_continue:
    var1 = input('введите строку чисел разделенных пробелом, для выхода нажмите q:')
    q_position = var1.find('q')
    if q_position > -1:
        is_continue = False
        var1 = var1[0: q_position]
    for value in var1.split():
        list_var.append(int(value))
    print(f'Сумма всех введенных числел:{sum(list_var)}')



