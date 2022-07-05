n = int(input())
ls = []
max_ls = []
mx = 0
b_mx = 0
max_i = 0
max_j = 0
max_tmp = 0
tmp_i = 0
tmp_j = 0
next_i = 0
next_j = 0
b_i = 0
b_j = 0

for i in range(n):
    num = [int(i) for i in list(input())]
    ls.append(num)
    if max(ls[i]) > max_tmp:
        max_tmp = max(ls[i])
        max_i = i
        max_j = ls[i].index(max_tmp)

for k in range(n):
    max_ls.append(max_tmp)
    print(max_tmp)
    max_tmp = 0
    if(next_i == 0 and next_j == 0):
        for i in range(-1,2):
            tmp_i = max_i + i
            if tmp_i < 0:
                tmp_i = n-1
            elif tmp_i > n-1:
                tmp_i = 0
            for j in range(-1,2):
                tmp_j = max_j + j
                if tmp_j < 0:
                    tmp_j = n-1
                elif tmp_j > n-1:
                    tmp_j = 0

                if ls[tmp_i][tmp_j] > max_tmp and ls[tmp_i][tmp_j] != mx and j != 0 and i != 0:
                    max_tmp = ls[tmp_i][tmp_j]
                    next_i = i
                    next_j = j
    else:
        tmp_i += next_i
        tmp_j += next_j
        print("a",tmp_i)
        if tmp_i < 0:
            tmp_i = n-1
        elif tmp_i > n-1:
            tmp_i = 0
        print("b",tmp_i)
        if tmp_j < 0:
            tmp_j = n-1
        elif tmp_j > n-1:
            tmp_j = 0

        max_tmp = ls[tmp_i][tmp_j]
        print("c",max_tmp)

print(next_i,next_j)
sum_number = int("".join([str(n) for n in max_ls]))
print(sum_number)