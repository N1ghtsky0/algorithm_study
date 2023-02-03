# Baekjoon 9465
# https://www.acmicpc.net/problem/9465

from sys import stdin
input = stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [[0] + [*map(int, input().split())] for _ in range(2)]
    for idx in range(n - 1):
        stickers[0][idx+2] += max(stickers[1][idx], stickers[1][idx + 1])
        stickers[1][idx + 2] += max(stickers[0][idx], stickers[0][idx + 1])
    print(max(stickers[0][-1], stickers[1][-1]))
