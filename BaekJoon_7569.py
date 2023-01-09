# Baekjoon 7569
# https://www.acmicpc.net/problem/7569

from collections import deque
from sys import stdin

input = stdin.readline

M, N, H = map(int, input().split())
tomato_field = [[input().split() for _ in " " * N] for _ in " " * H]

bfs = deque([])
for i, floor in enumerate(tomato_field):
    for n, line in enumerate(floor):
        idx = 0
        for _ in range(line.count("1")):
            bfs.append((i, n, line[idx:].index("1") + idx))
            idx += line[idx:].index("1") + 1

answer = -1

while bfs:
    l = len(bfs)
    for _ in " " * l:
        i, m, n = bfs.popleft()

        tmp = [(max(0, i-1), m, n)      # under
               , (min(i+1, H-1), m, n)    # over
               , (i, max(0, m-1), n)    # down
               , (i, min(m+1, N-1), n)    # up
               , (i, m, max(0, n-1))    # left
               , (i, m, min(n+1, M-1))    # right
               ]

        for t_i, t_m, t_n in tmp:
            if tomato_field[t_i][t_m][t_n] == "0":
                bfs.append((t_i, t_m, t_n))
                tomato_field[t_i][t_m][t_n] = "1"

    answer += 1

for t in tomato_field:
    for r in t:
        if "0" in r:
            answer = -1

print(answer)
