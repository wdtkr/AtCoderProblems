n,k,q = map(int,input().split())
ls_A = list(map(int,input().split()))
ls_Q = list(map(int,input().split()))

for i in range(q):
    if ls_A[ls_Q[i]-1] < n and ls_A.count(ls_A[ls_Q[i]-1]+1) == 0:
        ls_A[ls_Q[i]-1] += 1

print(*ls_A)