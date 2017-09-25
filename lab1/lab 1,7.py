import math
a = float(input())
b = float(input())
c = input()
if c == ('+'):
    print(a + b)
if c == ('*'):
    print(a * b)
if c == ('-'):
    print(a - b)
if c == ('/') and b == 0:
    print('Деление на ноль!')
elif c == ('/'):
    print(a / b)
if c == ('mod') and b == 0:
    print('Деление на ноль!')
elif c == ('mod'):
    print(a % b)
if c == ('pow'):
    print(pow(a,b))
if c == ('div') and b == 0:
    print('Деление на ноль!')
elif c == ('div'):
    print(a//b)

