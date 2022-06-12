n = int(input())
ls = list()
count = 0

for x in range(n):
    num = int(input())
    if ls.count(num) == 0:
        ls.append(num)
        
ls = sorted(ls, reverse=True)

for num in ls:
    count += 1

print(count)