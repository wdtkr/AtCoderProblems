import math
n,x = map(int,input().split())

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str[math.ceil(x/n -1)])