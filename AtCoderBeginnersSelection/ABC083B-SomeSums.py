n,a,b = map(int,input().split())
ans = 0

for x in range(n+1):
    sum = 0

    for y in str(x):
        sum += int(y)

    print("x:",x,",sum:",sum)
    if a <= sum <= b:
        ans += x

print(ans)