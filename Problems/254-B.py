n = int(input())
ls = []
ls_tmp = []

for n1 in range(n):
    ls = []
    if n1 == 0:
        # 一回目
        ls.append(1)
    elif n1 == 1:
        # 二回目
        ls.append(1)
        ls.append(1)
    else:
        # 三回目以降
        for n2 in range(n1+1):
            # 最初または最後の時必ず１
            if n2 == 0 or n2 == n1:
                ls.append(1)
            else:
                ls.append(ls_tmp[n2]+ls_tmp[n2-1])

    ls_tmp = ls
    for i in ls:
        print(i,end=' ')
    print()