orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
return_ist = [el for i, el in enumerate(orig_list[1:]) if el > orig_list[i-1]]
print(return_ist)
