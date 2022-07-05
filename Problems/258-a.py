n = int(input())

h = 21
m = 0

h += int(n/60)
m = n%60
if m < 10:
    print("%d:0%d"%(h,m))
else:
    print("%d:%d"%(h,m))