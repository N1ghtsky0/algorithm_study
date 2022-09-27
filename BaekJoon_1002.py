# Baekjoon 1002
# https://www.acmicpc.net/problem/1002

import math
T = int(input())
for _ in range(T):
  x1,y1,r1,x2,y2,r2 = map(int, input().split())
  d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  if x1==x2 and y1==y2 and r1==r2: print(-1)
  elif d > r1+r2: print(0)
  elif d == r1+r2: print(1)
  elif d < r1+r2:
    if abs(r1-r2) > d: print(0)
    elif abs(r1-r2) == d: print(1)
    else: print(2)
