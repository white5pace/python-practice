a = 'aaaabbcaa'
i = 0

while i < len(a):
    tek = a[i]
    counter = 1
    while tek == a[i]:
        counter += 1
        i += 1
    print(a[i], counter)

