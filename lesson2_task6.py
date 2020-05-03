is_continue=True
product_list=[]
while is_continue:
    name=input('Введите название товара:')
    cost = float(input('Введите цену:'))
    count = int(input('Введите колличество едениц'))
    unit = input('введите еденицу измерения') #вот тут по хорошему ограничить пространство выбора, но на обчении такой возможности не рассматривали. можно через кортеж, но куча условий свалидацией результата силь увелит размер задания.
    replay = input('Прдолжим? (да/нет):').lower().strip()
    is_continue = True if replay == 'да' else False
    product = {'Название': name, 'цена': cost, 'Колличество': count, 'еденицы измерения': unit}
    product_list.append(product)
#получим список ключей ибо указывать их руками неправильно )структура данных может измениться
key_set=set()
for cur_product in product_list:
    #в теории набор ключей для разных продуктов может изменсять поэтому пройдем весь список
    for key in cur_product.keys():
        key_set.add(key)
#а теперь еще раз пройдем ко списку продуктов и посчитаем ключи
analytics_dict = {}
for key in key_set:
    value_list = []
    for cur_product in product_list:
        value = cur_product.get(key)
        value_list.append(value)
    analytics_dict.update({key: value_list})
#выводим результат
print('Результат:')
for key, value in analytics_dict.items():
    print(f'{key}: {value}')