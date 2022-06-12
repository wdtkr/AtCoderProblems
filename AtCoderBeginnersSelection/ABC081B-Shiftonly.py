a = int(input())
# num = [a]
num = input().split()
count = 0
flg = True

while flg:
    i = 0
    for x in num:
        x = int(x)

        if x % 2 != 0:
            flg = False

        num[i] = x/2

        i = i + 1
        
    if flg == False:
        break
    count = count + 1
print(count)