var=int(input('ВВедите простое число:'))
var_var=int(f'{var}{var}')
var_var_var=int(f'{var}{var}{var}')
result=var+ var_var+var_var_var
print(result)