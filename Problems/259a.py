N,M,X,T,D = map(int,input().split())
ans = T
tmp = N

if X < M:
    ans = T
else:
    ans -= ( X - M ) * D

print(ans)