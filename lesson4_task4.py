src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [el for el in src_list if src_list.count(el) == 1]
print(list2)