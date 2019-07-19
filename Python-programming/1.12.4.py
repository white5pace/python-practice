shape = input()

if shape == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif shape == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif shape == 'круг':
    r = int(input())
    print((r ** 2) * 3.14)
else:
    print('Данные введены неверно')
