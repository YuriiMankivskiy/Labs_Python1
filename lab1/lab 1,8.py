import math
x = input()
pi = 3.14
if x == ('треугольник'):
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    p = (a + b + c)/2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
if x == ('круг'):
    r = int(input('r = '))
    krug = pi * pow(r,2)
    print(krug)
if x == ('прямоугольник'):
    a = float(input('a = '))
    b = float(input('b = '))
    print(a*b)
