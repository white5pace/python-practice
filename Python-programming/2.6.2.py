# Мое решение
a, i, n = int(input()), 0, 1
while i < a:
    z = 0
    while (z < n or z == 0) and (z+i < a):
        print(n, end = ' ')
        z += 1
    n += 1
    i += z
# 2 решение 
# n, x = int(input()), []
# for i in range(n+1):
#     x += [i] * i
# print(x)
# print(*x[:n])