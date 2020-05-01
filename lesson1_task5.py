profit_var=float(input('Введите выручку:'))
cost_var=float(input('Введите изрежки:'))
effective_var=profit_var-cost_var
if profit_var> cost_var:
    print(f'прибыль составила: {effective_var}')
    print(f'Рентабельность выручки: {profit_var/cost_var:.2f}')
    count_emp=int(input('Введите колличество сотрудников фирмы:'))
    print(f'Прибыль на сотрудника: {effective_var/count_emp:.2f}')
elif profit_var==cost_var:
    print('фирма сработала в 0')
else:
    print(f'Фирма сработала в убыток: {effective_var*-1}')