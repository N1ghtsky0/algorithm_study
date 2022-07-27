# BaekJoon 11047
# https://www.acmicpc.net/problem/11047

from sys import stdin
n, k = map(int, input().split())
coins = [int(stdin.readline().rstrip()) for _ in range(n)]
result = 0
for coin in coins[::-1]:
    result += k // coin
    k %= coin
    if k == 0: break
print(result)
