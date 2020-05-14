import requests
import json
try:
    file = open(r'c:\temp\example\text_4.txt', encoding='utf-8')
    for line in file:
        print(line)
        list_word = line.split('-')
        word = list_word[0]
        digit = int(list_word[1])
        resp = requests.get(f'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200514T123433Z.d36d6fd0823b1012.f54a1610355d495e4dd02f444d7ba25e33842aa4&text={word}&lang=en-ru&format=plain')
        translate_word = json.loads(resp.content.decode()).get('text')[0]
        file_result = open(r'c:\temp\example\text_4_result.txt', encoding='utf-8', mode='a')
        file_result.writelines([translate_word, '- ', str(digit), '\n'])
except IOError:
    print('Ошибка ввода/вывода!')
finally:
    file.close()
    file_result.close()
