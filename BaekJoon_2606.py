# Baekjoon 2606
# https://www.acmicpc.net/problem/2606

from collections import deque
from sys import stdin; input=stdin.readline
N = int(input())
connected_num = int(input().strip())

connected = {}

for _ in range(connected_num):
    a, b = map(int, input().split())
    if a not in connected:
        connected[a] = [b]
    else:
        connected[a].append(b)

    if b not in connected:
        connected[b] = [a]
    else:
        connected[b].append(a)

tmp = deque([1])
infected = []
while tmp:
    for c in connected[tmp.popleft()]:
        if c not in infected:
            infected.append(c)
            tmp.append(c)
print(len(infected)-1)
