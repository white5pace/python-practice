di = dict()
a = [i.lower() for i in input().split()]
for i in a:
    if i in di: 
        di[i] += 1
    else:
        di[i] = 1
for i in di:
    print(i, di.get(i))