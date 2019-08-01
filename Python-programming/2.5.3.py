b, c = [int(i) for i in input().split()], []
b.sort()
current = b[0]

for i in range(1, len(b)):
    if current == b[i]:
        if b[i] not in c:
            c.append(b[i])
    else:
        current = b[i]

for i in c:
    print(i, end=' ')
