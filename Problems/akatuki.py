from math import ceil

N,W = map(int,input().split())
ls = list(map(int,input().split()))
d = {}
count = 0
i = 0
for member in ls:
    i += 1
    ans = ceil(member / W)
    d[i] = ans

d2 = sorted(d.items(),key=lambda x:x[1])
# print(d2)
# print(type(d2))
# d2はリスト
for val in d2:
    print(val[0])
