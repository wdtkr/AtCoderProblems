x,y = map(int,input().split())
a,b = map(int,input().split())
c,d = map(int,input().split())

if x == 1:
    if y == 1:
        print(a)
    else:
        print(b)
else:
    if y == 1:
        print(c)
    else:
        print(d)
        