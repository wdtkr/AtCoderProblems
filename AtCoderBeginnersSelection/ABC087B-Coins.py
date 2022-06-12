a = int(input())
b = int(input())
c = int(input())
sum = int(input())

count = 0

for x in range(a+1):
    for y in range(b+1):
        for z in range(c+1):
            if (x*500)+(y*100)+(z*50) == sum:
                count+=1

print(count)

# 以下はボツ。
# # xが全て５０円玉で表せるとき
# if x / 50 <= c:
#     count += 1


# # xが少なくとも1枚の１００円を用いて表せる時
# while coins > 0:
#     coins -= 2
#     count_b += 1

#     if coins <= c and count_b <= b:
#         count += 1

# 以下が微妙に間違ってる
# # xが少なくとも1枚の5００円を用いて表せる時
# while count_a < a and tmp_x >= 500:
#     tmp_x -= 500
#     count_a += 1
#     count_b = 0
#     coins = tmp_x / 50
#     # ５００円を引いたものが全て５０円玉で表せるとき
#     if tmp_x / 50 <= c:
#         count += 1

#     # かつ、xが少なくとも1枚の１００円を用いて表せる時
#     while coins > 0:
#         coins -= 2
#         count_b += 1

#         if coins <= c and count_b <= b:
#             count += 1

# print(count)