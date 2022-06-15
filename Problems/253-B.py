h,w = map(int,input().split())
ls = []
count = 0
tmp1 = -1
tmp2 = -1
ans = 0

for i in range(h):
    ls.append(input())

for x in ls:
    if x.count('o') == 2:
        tmp1 = x.find('o')
        tmp2 = x.rfind('o')
        ans = abs(tmp1 - tmp2)
        break
    elif tmp1 == -1:
        tmp1 = x.find('o')
    elif tmp2 == -1:
        tmp2 = x.find('o')
        if tmp1 == tmp2:
            ans = count
            break
        elif tmp2 != -1:
            ans = count + abs(tmp1 - tmp2)
            break

    if tmp1 != -1:
        count += 1

print(ans)