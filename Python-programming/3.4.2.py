lines = ''

with open('bible.txt') as inf:
  for line in inf:
    line = line.strip()
    lines += line
mas = lines.lower().split()
di = dict()

for i in mas: 
  if i in di:
    di[i] += 1
  else:
    di[i] = 1
frequent = False
for i in di:
  if not frequent: 
    frequent = [i, di[i]]
  elif di[i] > frequent[1]:
    frequent = [i, di[i]]
  elif di[i] == frequent[1]:
    if i < frequent[0]:
      frequent = [i, di[i]]
# out = ''
# out += frequent[0]
# out += ' '
# out += str(frequent[1])
# print(out)
with open('ans2.txt', 'w') as ouf:
  ouf.write(print(frequent[0], frequent[1]))