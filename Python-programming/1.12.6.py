n = int(input())

if n < 20:
    n_mod = n
elif n >= 20 and n < 100:
    n_mod = n % 10
elif n >= 100 and n < 1000:
    n_mod = n % 100
    if not (n_mod > 10 and n_mod < 20):
        n_mod = n % 10
else:
    n_mod = n % 1000

if n_mod == 1:
    print(n, 'программист')
elif n_mod > 1 and n_mod < 5:
    print(n, 'программиста')
elif (n_mod >= 5 and n_mod <= 19) or n_mod == 0:
    print(n, 'программистов')