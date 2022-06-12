n,y = map(int,input().split())
man = -1
gosen = -1
sen = -1

for a in range(n+1):
    for b in range(n-a+1):
        c = n - (a + b)
        if a*10000 + b*5000 + c*1000 == y:
            man = a
            gosen = b
            sen = c

print(man,gosen,sen)