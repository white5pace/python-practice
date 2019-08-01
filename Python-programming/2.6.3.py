lst = [int(i) for i in input().split()]
x = int(input())
trig = True
for i in range(len(lst)):
  if lst[i] == x:
    trig = False
    print(i, end=' ')
if trig:
  print('Отсутствует')
  