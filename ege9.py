file = open("test9.txt")
res = 0
for s in file:
    sp = [int(x) for x in s.split()]
    if len(sp) == len(set(sp)):
        ch = [int(x) for x in sp if x % 2 == 0]
        nech = [int(x) for x in sp if x % 2 != 0]
        if len(nech) > len(ch) and sum(nech) < sum(ch):
            res += 1
print(res)
