# BaekJoon 1149
# https://www.acmicpc.net/problem/1149

from sys import stdin; s_input=stdin.readline
N = int(input())
RGB = [list(map(int, s_input().rstrip().split())) for _ in range(N)]

for n in range(1, N):
    RGB[n][0] += min(RGB[n-1][1], RGB[n-1][2])
    RGB[n][1] += min(RGB[n-1][0], RGB[n-1][2])
    RGB[n][2] += min(RGB[n-1][0], RGB[n-1][1])
print(min(RGB[-1]))
