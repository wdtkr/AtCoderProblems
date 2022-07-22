N,X,Y,Z = map(int,input().split())
math_ls = list(map(int,input().split()))
eng_ls = list(map(int,input().split()))
both_ls = []
ans_ls = []
j = 0
tmp = 0

math_ls_down = sorted(math_ls,reverse=True)
eng_ls_down = sorted(eng_ls,reverse=True)

for i in range(X):
    ans_ls.append(math_ls.index(math_ls_down[i])+1)
    math_ls[math_ls.index(math_ls_down[i])] = -9999

for i in range(Y):
    if j!=0:
        j += 1
    print(eng_ls_down[j])
    print(eng_ls_down)
    if math_ls[eng_ls.index(eng_ls_down[j])] == -9999:
        tmp = 1
    else:
        tmp = 0
    j += tmp
    ans_ls.append(eng_ls.index(eng_ls_down[j])+1)
    eng_ls[eng_ls.index(eng_ls_down[j])] = -9999
    print(eng_ls_down[j])
    

for i in range(N):
    both_ls.append(math_ls[i]+eng_ls[i])

both_ls_down = sorted(both_ls,reverse=True)

for i in range(Z):
    ans_ls.append(both_ls.index(both_ls_down[i])+1)
    both_ls[both_ls.index(both_ls_down[i])] = -9999


ans_ls.sort()
for index in ans_ls:
    print(index)
