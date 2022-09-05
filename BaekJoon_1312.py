# BaekJoon 1312
# https://www.acmicpc.net/problem/1312

a, b, n = map(int, input().split())
r = 0
for _ in range(n):
    a = (a % b) * 10
    r = a // b
print(r)
