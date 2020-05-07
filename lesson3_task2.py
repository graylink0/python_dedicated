def print_user_data(first_name, sec_name, year_born, city, email, phone):
    """Выводим на экран данные пользователя
    :param
    first_name - имя
    sec_name -фамилия
    year_born -год рождения
    city - город проживания
    email - электронная почта
    phone - номер телефона
    """
    print(
        f'Имя: {first_name}, фамилия: {sec_name}, год рождения: {year_born}, город проживания: {city}, электронная почта: {email} телефонный номер: {phone}')


first_name = input('Введите имя:')
sec_name = input('Введите фамилию:')
year_born = input('Введите год рождения:')
city = input('Введите город проживания:')
email = input('Введите адрес электронной почты:')
phone = input('Введите номер телефона:')
print_user_data(first_name=first_name, sec_name=sec_name, year_born=year_born, city=city, email=email, phone=phone)

