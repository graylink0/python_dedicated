def calculate_sum(file_path):
    try:
        file = open(file_path, mode='r')
        for line in file:
            digit_list = map(float, line.split())
    except IOError:
        print('Ошибка ввода/вывода')
    finally:
        file.close()
        return sum(digit_list)


def write_digit_to_file(file_path, digit_list):
    try:
        file = open(file_path, mode='w')
        file.writelines(digit_list)
    except IOError:
        print('Ошибка ввода/вывода!')
    finally:
        file.close()


file_str = r'c:\temp\lesson6.txt'
input_digits = input('Введите последовательность цифр разделенных пробелом:')
write_digit_to_file(file_str, input_digits)
print(calculate_sum(file_str))
