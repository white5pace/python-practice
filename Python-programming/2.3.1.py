a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(' ', end=' ')
for f in range(c, d+1):
    print(f, end=' ')
print()
for i in range(a, b+1):
    print(i, end=' ')
    for z in range(c, d+1):
        print(i*z, end=' ')
    print()