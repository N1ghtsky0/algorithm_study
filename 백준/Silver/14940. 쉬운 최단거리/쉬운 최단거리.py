from collections import deque
from sys import stdin

rd = stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

n, m = map(int, rd().rstrip().split())
MAP = []
target = ()

for row in range(m):
    line = list(map(int, rd().rstrip().replace('1', '-1').split()))
    if 2 in line:
        target = (row, line.index(2))
        line[line.index(2)] = 0
    MAP.append(line)

q = deque([target])

while q:
    r, c = q.popleft()
    for mv_idx in range(4):
        nr = r + dr[mv_idx]
        nc = c + dc[mv_idx]
        if 0 <= nr < n and 0<= nc < m and MAP[nr][nc] == -1:
            MAP[nr][nc] = MAP[r][c] + 1
            q.append((nr, nc))

for line in MAP:
    print(' '.join(list(map(str, line))))