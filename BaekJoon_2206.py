# Baekjoon 2206
# https://www.acmicpc.net/problem/2206

from sys import stdin
from collections import deque

def bfs():
    global answer
    while Q:
        answer += 1
        step = len(Q)
        for _ in " " * step:
            x, y, broken = Q.popleft()
            if (x, y) == (N - 1, M - 1):
                return True

            for dx, dy in mv:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not (nx, ny, broken) in VISITED:
                    VISITED.add((nx, ny, broken))
                    if MAP[nx][ny] == "1":
                        if not broken:
                            Q.append((nx, ny, True))
                    else:
                        Q.append((nx, ny, broken))
    return False

rd = stdin.readline
Q = deque()

N, M = map(int, input().split())
MAP = [rd().strip() for _ in " " * N]
VISITED = set()
mv = [(0, -1), (0, 1), (1, 0), (-1, 0)]

Q.append((0, 0, False))
answer = 0
result = bfs()
print(answer if result else -1)
