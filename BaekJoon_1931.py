# Baekjoon 1931
# https://www.acmicpc.net/problem/1931

from sys import stdin
input = stdin.readline

info = [list(map(int, input().split())) for _ in ' ' * int(input())]
info.sort(key=lambda x: (x[1], x[0]))
answer = 0
end = 0

for s, e in info:
    if s >= end:
        answer += 1
        end = e

print(answer)
