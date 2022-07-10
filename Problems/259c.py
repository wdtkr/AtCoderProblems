ls_in = list(input())
ls_ans = list(input())
tmp = ""
in_count = 1
ans_count = 1
in_ls = []
ans_ls = []
ans = "No"
flg = True

for st in ls_in:
    # print(st,tmp)
    if tmp == "":
        in_count = 1
    elif tmp == st:
        # 前の項と同じなら１＋
        in_count += 1
    else:
        # 違うなら追加
        in_ls.append([in_count,tmp])
        in_count = 1
    tmp = st

in_ls.append([in_count,tmp])

tmp = ""
for st in ls_ans:
    # print(st,tmp)
    if tmp == "":
        ans_count = 1
    elif tmp == st:
        # 前の項と同じなら１＋
        ans_count += 1
    else:
        # 違うなら追加
        ans_ls.append([ans_count,tmp])
        ans_count = 1
    tmp = st
ans_ls.append([ans_count,tmp])

if len(in_ls) == len(ans_ls) and flg:
    for i in range(len(in_ls)):
        if in_ls[i][1] == ans_ls[i][1]:
            if in_ls[i][0] == ans_ls[i][0]:
                ans = "Yes"
            elif in_ls[i][0] >= 2 and in_ls[i][0] <= ans_ls[i][0]:
                ans = "Yes"
            else:
                ans = "No"
                break
        else:
            ans = "No"
            break

        if ans == "No":
            break
    
print(ans)