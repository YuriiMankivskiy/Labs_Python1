m = input()
n = int(m[-2:])
stov = {5, 6, 7, 8, 9}
if n // 10 == 1 or n % 10 == 0 or n % 10 in stov:
     print (m + " программистов")
elif n % 10 == 1:
     print (m + " программист")
else:
     print (m + " программиста")
