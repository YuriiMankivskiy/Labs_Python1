x = int(input('x='))
h = int(input('h='))*60
m = int(input('m='))
a = (h + m + x)//60
b = (h + m + x)%60
print(a,b)
