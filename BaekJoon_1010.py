# Baekjoon 1010
# https://www.acmicpc.net/problem/1010

from sys import stdin
input = stdin.readline

factorial = [1, 1, 2, 6]
for i in range(4, 31):
    factorial.append(factorial[-1] * i)

for _ in ' ' * int(input()):
    N, M = map(int, input().split())
    print(factorial[M]//(factorial[N] * factorial[M-N]))
