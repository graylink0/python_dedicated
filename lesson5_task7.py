import json


def get_all_firms(file_path) -> list:
    firms_list = []
    try:
        file = open(r'c:\temp\example\text_7.txt', mode='r', encoding='utf-8')
        for line in file:
            line_split = line.split()
            full_firm_name = line_split[1] + ' ' + line_split[0]
            firm_profit = float(line_split[2]) - float(line_split[3])
            firms_list.append({full_firm_name: firm_profit})
    except IOError:
        print('Ошибка ввода/вывода')
    finally:
        file.close()
        return firms_list


def get_average_profit(all_firms):
    sum_profit = 0
    for firm in all_firms:
        profit = sum(dict(firm).values())
        if profit >= 0:
            sum_profit = sum_profit + profit  # не уверен что правильно считать нулевые значения, но допустим..
    return {'average_profit': sum_profit}


def save_to_file(path_to_file, result_list):
    with open(path_to_file, 'w') as file:
        json.dump(result_list, file, sort_keys=True, ensure_ascii=False, indent=4)


result_list = []
file_path = r'c:\temp\example\text_7.txt'
all_firms = get_all_firms(file_path)
result_list = all_firms
result_list.append(get_average_profit(all_firms))
save_to_file(r'c:\temp\task7.json', result_list)

