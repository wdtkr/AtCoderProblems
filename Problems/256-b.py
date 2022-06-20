n = int(input())
A_ls = list(map(int, input().split()))
p = 0

for i in range(n):
    tmp = 0
    for num in A_ls[i:n]:
        tmp += num
        if tmp >= 4:
            break
    if tmp >= 4:
        p += 1

print(p)