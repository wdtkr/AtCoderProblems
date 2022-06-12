x,a,d,n = map(int,input().split()) # 整数x　初項A　公差D　項数N 
x -= a # xから初項を引くことで、初項を0にした場合として考えられる
last = d * (n-1) #末項　aは0のため足さない

if d==0:
    ans = abs(x)
elif 0 <= x <= last or 0 >= x >= last:
# 範囲外でないなら
    ans = min(abs(x) % abs(d),abs(d)-(abs(x) % abs(d)))
else:
    ans = min(abs(0-x),abs(last-x))
print(ans)