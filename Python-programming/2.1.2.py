a, b = int(input()), int(input())

i, mod = 0, 1
while mod > 0:
    i += 1
    mod = i % a + i % b

print(i)
