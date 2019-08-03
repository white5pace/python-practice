def f(x):
  return x * 10

n = int(input())
di = dict()
for i in range(n):
    x = int(input())
    if x not in di:
        di[x] = f(x)
    print(di[x])