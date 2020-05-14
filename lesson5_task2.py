try:
    file = open(r'c:\temp\task1.txt', 'r')
    count_lines = 0
    count_words_dict = {}
    for line in file:
        print(line)
        count_lines += 1
        words = line.split()
        count_words = len(words)
        count_char_dirty = len(line) #с пробелами и знаками припинания
        count_char = 0
        for char in line:
            if char.isalnum(): #числа знаки
                count_char += 1
        count_words_dict.update({count_lines: {'count_words': count_words, 'count_char': count_char}})
except IOError:
    print('Ошибка ввода/вывода!')
finally:
    file.close()
    print(f'В файле {count_lines} строк.')
    for line in count_words_dict.keys():
        count_words = count_words_dict.get(line).get('count_words')
        count_char = count_words_dict.get(line).get('count_char')
        print (f'В {line} строке, {count_words} слов и {count_char} символов (буквенно числовых)')