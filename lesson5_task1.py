need_continue = True
try:
    file = open('c:\\temp\\task1.txt', 'a')
    while need_continue:
        str_line = input('Введите новую строку:')
        print (str_line)
        if len(str_line) == 0:
            need_continue = False
        file.writelines([str_line, '\n'])

except IOError:
    print('Ошибка ввода/вывода!')
finally:
    file.close()
