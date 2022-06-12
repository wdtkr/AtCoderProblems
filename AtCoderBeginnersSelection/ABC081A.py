num = int(input())
count = 0

if (num - 100) >= 0 :
    count = count + 1
    num -= 100

if num - 10 >= 0 :
    count = count + 1
    num -= 10

if num == 1 :
    count = count + 1

print(count)