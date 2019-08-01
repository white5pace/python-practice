a = []
while True:
    inp = input()
    if inp == 'end':
        break;
    b = [int(i) for i in inp.split()]
    a.append(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        s = a[i-1][j] + a[i+1-len(a)][j] + a[i][j-1] + a[i][j+1-len(a[i])]
        print(s,end = ' ')
    print()