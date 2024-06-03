# максимальная сумма в массиве
# j < i
# l[i] + l[j] -> max

sp = input().split()
n = int(sp[0])
k = int(sp[1])
l = input().split()
ibest = 1
jbest = 0
imax = 0

for i in range(k+1, len(l)):
  if l[i - 1] > l[imax]:
    imax = i - k
  if l[i] + l[imax] > l[ibest] + l[jbest]:
    ibest = i
    jbest = imax

print(jbest + 1, ibest + 1)