b = [int(i) for i in input().split()]
for i in range(0, len(b)):
    if len(b) <= 1:
        print(b[i], end=' ')
    elif i == len(b)-1:
        print(b[i-1] + b[0], end=' ')
    else:
        print(b[i-1] + b[i+1], end=' ')