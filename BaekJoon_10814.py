# BaekJoon 10814
# https://www.acmicpc.net/problem/10814

from sys import stdin; s = stdin.readline
print('\n'.join(sorted([s().rstrip() for _ in range(int(input()))], key = lambda x: int(x.split()[0]))))
