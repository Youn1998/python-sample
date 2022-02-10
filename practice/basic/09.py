d = {}
n = 1
for i in range(1,31):
  if i % 3 == 0:
    d['{}番目'.format(n)] = i
    n += 1
print(d)