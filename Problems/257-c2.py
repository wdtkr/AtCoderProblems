N = int(input())
S = input()
W = list(map(int, input().split()))
S_W = []
ans = S.count("1")
for i in range(N):
    S_W.append((W[i], S[i]))
 
S_W.sort()
print(S_W)