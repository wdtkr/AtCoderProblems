n = int(input())
ls = list(map(int,input().split()))
ls = sorted(ls, reverse=True)

ans = 0

i = 0

for n in ls:
    if i % 2 == 0:
        ans += n
    elif i % 2 == 1:
        ans -= n
    i+=1

print(ans)