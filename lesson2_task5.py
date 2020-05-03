#вот не понял должен ли рейтинг быть проинициализирован значениями по умолчанию или он должен формировать по мере ввода
#предположил второй вариант
rating = []
replay = 'да'
while replay == 'да':
    new_value = int(input('Введите новое значение для рэйтинга:'))

    if len(rating) == 0:
        rating.insert(0, new_value)
    else:
        q=len(rating)
        for i in range(len(rating), 0, -1):
            if new_value >=rating[i-1]:
                rating.insert(i, new_value)
                break
            if i == 1:
                rating.insert(0, new_value)
    print('рейтинг:')
    print(rating)
    replay = input('Прдолжим? (да/нет):').lower().strip()
print('рейтинг:')
print(rating)



