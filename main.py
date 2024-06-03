# максимальная сумма в массиве
# j < i
# l[i] - l[j] -> max

l = []
sp = input().split()
n = int(sp[0])
k = int(sp[1])
l = [int(i) for i in input().split()]
ibest = k+1
jbest = 0
imax = 0

for i in range(k+1, len(l)):
  if l[i - k - 1] > l[imax]:
    imax = i - k - 1
  if l[i] + l[imax] > l[ibest] + l[jbest]:
    ibest = i
    jbest = imax

print(jbest + 1, ibest + 1)
