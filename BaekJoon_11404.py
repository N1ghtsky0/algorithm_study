# Baekjoon 11404
# https://www.acmicpc.net/problem/11404

import sys
from sys import stdin

rd = stdin.readline
INF = sys.maxsize
n = int(rd())
answer = [[INF] * n for _ in " " * n]
for idx in range(n):
    answer[idx][idx] = 0

m = int(rd())
for _ in " " * m:
    a, b, c = map(int, rd().split())
    if answer[a-1][b-1] > c:
        answer[a-1][b-1] = c

for i in range(n):
    for j in range(n):
        for k in range(n):
            if answer[j][k] > answer[j][i] + answer[i][k]:
                answer[j][k] = answer[j][i] + answer[i][k]

for row in answer:
    print(" ".join([str(a) if a != INF else "0" for a in row]))
