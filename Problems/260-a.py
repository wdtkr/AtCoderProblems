a = list(input())
tmp = -1
for st1 in a:
    count = 0
    for st2 in a:
        if st1 == st2:
            count+=1
    if count == 1:
        print(st1)
        tmp = 1
        break

if tmp == -1:
    print(tmp)
