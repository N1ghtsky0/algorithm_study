# Baekjoon 2563
# https://www.acmicpc.net/problem/2563

from sys import stdin; input=stdin.readline
white = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input().strip())):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            white[j][i] = 1
print(sum([sum(row) for row in white]))
