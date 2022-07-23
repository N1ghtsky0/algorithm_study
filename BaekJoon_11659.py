# BaekJoon 11659
# https://www.acmicpc.net/problem/11659

from sys import stdin
N, M = map(int, input().split())
num = list(map(int, input().split()))

R = [0]
for idx, n in enumerate(num):
    R.append(R[idx] + n)

for _ in range(M):
    s, e = map(int, stdin.readline().rstrip().split())
    print(R[e] - R[s-1])
