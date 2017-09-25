a = int(input('A = '))
b = int(input('B = '))
c = a*b
while a!=0 and b!=0:
    if a > b:
        a = a % b
    else:
        b = b % a
print (c/(a+b))
