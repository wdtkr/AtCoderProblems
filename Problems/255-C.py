x,a,d,n = map(int,input().split())
ls = []
num = a
min = 1000000000000000000000000

for i in range(n):
    ls.append(num)
    num += d

for i in ls:
    tmp = abs(i - x)
    if min > tmp:
        min = tmp

print(min)