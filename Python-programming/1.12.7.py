ticket = int(input())

a = ticket // 100000
b = (ticket // 10000) % 10
c = ((ticket // 1000) % 100) % 10
d = ticket % 1000 // 100
e = ticket % 100 // 10
f = ticket % 10

if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')