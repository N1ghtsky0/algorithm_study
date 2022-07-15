# BaekJoon 2981
# https://www.acmicpc.net/problem/2981

import math

num = sorted([int(input()) for _ in range(int(input()))])
dif = [num[i] - num[i-1] for i in range(1, len(num))]

gcd = dif[0]
for i in range(1, len(dif)):
    gcd = math.gcd(gcd, dif[i])

result = [str(gcd)]
for i in range(2, int(gcd ** (1/2)) + 1):
    if gcd % i == 0:
        result.append(str(i))
        result.append(str(gcd // i))
print(' '.join(sorted(list(set(result)), key = lambda x : int(x))))
