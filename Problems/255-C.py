def comp(num,x,d):
    tmp = 0 #一個前のnumを保存
    if d > 0:
        while num <= x:
            tmp = num
            num += d
    else:
        while num >= x:
            tmp = num
            num += d
        
    if abs(tmp - x) <= abs(num - x):
        # tmpの方が近い時
        ans = tmp - x
    else:
        ans = num - x
    return ans

x,a,d,n = map(int,input().split())
# # 整数x　初項A　公差D　項数N 
last = a + (d * (n-1)) #末項
mid = a + (d * int(n / 2)) #中間

# 公差が正の時
if d >= 0:
    # 末項より大きい時
    if last <= x:
        ans = abs(x - last)
    # 中間より大きい時
    elif mid <= x:
        ans = comp(mid,x,d)
    # 初項より大きい時
    elif a <= x:
        ans = comp(a,x,d) 
    # 初項より小さい時
    else:
        ans = abs(x - a)
else:
    # 末項より小さい時
    if last >= x:
        ans = abs(x - last)
    # 中間項より小さい時
    elif mid >= x:
        ans = comp(mid,x,d)
    # 初項より小さい時
    elif a >= x:
        ans = comp(a,x,d)
    # 初項より大きい時
    else:
        ans = abs(x - a)

print(ans)