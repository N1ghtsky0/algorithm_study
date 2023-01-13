# Baekjoon 1389
# https://www.acmicpc.net/problem/1389

from sys import stdin
from collections import deque

rd = stdin.readline
N, M = map(int, rd().split())
Kevin_Bacon = [0] * (N + 1)
Kevin_Bacon[0] = 5001
connections = {idx: [] for idx in range(1, N + 1)}

for _ in " " * M:
    A, B = map(int, rd().split())
    connections[A].append(B)
    connections[B].append(A)

for n in range(1, N + 1):
    num = 0
    visited = [False] * (N + 1)
    visited[n] = True

    tmp = deque([n])
    while tmp:
        num += 1
        l = len(tmp)
        for _ in " " * l:
            current = tmp.popleft()
            for next in connections[current]:
                if not visited[next]:
                    tmp.append(next)
                    visited[next] = True
                    Kevin_Bacon[n] += num

print(Kevin_Bacon.index(min(Kevin_Bacon)))
