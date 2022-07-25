# BaekJoon 10773
# https://www.acmicpc.net/problem/10773

from sys import stdin
k = int(input())
lst = []
for _ in range(k):
    n = int(stdin.readline().rstrip())
    if n == 0:
        lst.pop()
    else:
        lst.append(n)
print(sum(lst))
