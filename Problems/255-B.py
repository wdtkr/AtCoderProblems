import numpy as np

n,k = map(int,input().split())
A_ls = input().split()
pos_all = []
pos_have = []
pos_all_i = []
pos_have_i = []
min = 0
dist_ls = []

for i in range(n):
    pos_all.append(input().split())

for i in A_ls:
    pos_have.append(pos_all[int(i)-1])

for tmp in pos_all:
    pos_all_i.append([int(s) for s in tmp])

for tmp in pos_have:
    pos_have_i.append([int(s) for s in tmp])

for i in range(n):
    if (pos_all_i[i] in pos_have_i) == False:
        min = 0.0
        # print(i,"番目の人はライト持ってないよ")
         # 今見てる人がライトをもっていないなら
        for have in pos_have_i:
            # ライトを持ってる人と距離を比べる
            dist = np.sqrt(np.sum(np.square(np.array(pos_all_i[i]) - np.array(have))))
            if min == 0:
                # 1人目なら初期値で距離設定
                min = dist
            elif dist < min:
                min = dist
        dist_ls.append(min)
# 一番近い人リストの中で一番遠い距離を探す
print(max(dist_ls))