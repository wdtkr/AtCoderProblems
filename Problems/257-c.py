n = int(input())
ls_S = list(input())
ls_W = list(map(int,input().split()))
x = min(ls_W)
max_num = 0
ls_Ans = []
tmp = []
for num in range(n):
    ls_Ans.append("0")

tmp = list(ls_Ans)
for i in range(max(ls_W) - min(ls_W)+10):
    count = 0
    ls_Ans = list(tmp)
    for j in range(len(ls_W)):
        if ls_W[j] >= x:
            ls_Ans[j] = "1"
        if ls_Ans[j] == ls_S[j]:
            count += 1
    if count >= max_num:
        max_num = count
    x += 1

print(max_num)