a, b = int(input()), int(input())
s, c = 0, 0
for i in range(a, b+1):
    if i % 3 == 0:
        s += i
        c += 1

print(s / c)