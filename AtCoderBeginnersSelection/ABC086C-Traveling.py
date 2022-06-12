from time import time

n = int(input())
times = [0]
x_ls = []
y_ls = []

now_pos = [0,0]
for tmp in range(n):
    t,x,y= map(int,input().split())
    times.append(t)
    x_ls.append(x)
    y_ls.append(y)

# 目的地と現在地の差が偶数の時，偶数回のtimesかつtime >+ x+yのとき行ける
for tmp in range(n):
    # print(now_pos[0]+now_pos[1],"-",x_ls[tmp]+y_ls[tmp],"%2 = ",(now_pos[0]+now_pos[1] - x_ls[tmp]+y_ls[tmp])%2,"==",(times[tmp+1] - times[tmp]) % 2)
    if ((now_pos[0]+now_pos[1] - x_ls[tmp]+y_ls[tmp])%2 == (times[tmp+1] - times[tmp])% 2) and times[tmp+1] - times[tmp] >= abs(x_ls[tmp]-now_pos[0]) + abs(y_ls[tmp]-now_pos[1]):
        st = "Yes"
        now_pos[0] = x_ls[tmp]
        now_pos[1] = y_ls[tmp]
    else:
        st = "No"
        break

print(st)