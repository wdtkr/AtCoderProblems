import numpy as np
a,b,d = map(int,input().split())

cos = np.cos(np.deg2rad(d))
sin = np.sin(np.deg2rad(d))

ans_a = (a * cos) - (b * sin)
ans_b = (a * sin) + (b * cos)

print(ans_a,ans_b)