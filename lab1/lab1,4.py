x = int(input('year - '))
if x % 4 == 0 and x % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
