#seconds_full=int(input('введите секунды:'))
seconds_full=8721
hours=seconds_full//3600
min=(seconds_full%3600)//(60)
sec=seconds_full%60
print (f'{hours}:{min}:{sec}')