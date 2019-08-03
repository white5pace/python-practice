with open('dataset_3363_2.txt') as inf:
  s1 = inf.readline().strip()

i = len(s1) - 1
digit = ''
save = []
while i >= 0:
  if '0' <= s1[i] <= '9':
    digit += s1[i] 
  else:
    save.append(s1[i] * int(digit[::-1]))
    digit = ''
  i -= 1
out = ''
for x in range(len(save) - 1,-1,-1):
  out += save[x]
with open('ans.txt', 'w') as ouf:
  ouf.write(out)