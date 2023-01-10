# Baekjoon 2667
# https://www.acmicpc.net/problem/2667

from collections import deque
from sys import stdin, stdout

input = stdin.readline

N = int(input())
home_map = [input() for _ in " " * N]
checked_map = [[False] * N for _ in " " * N]

initial_bfs = []

for n, line in enumerate(home_map):
    idx = 0
    for _ in range(line.count("1")):
        initial_bfs.append((n, line[idx:].index("1") + idx))
        idx += line[idx:].index("1") + 1

answer = []

for x, y in initial_bfs:
    if not checked_map[x][y]:
        bfs = deque([(x, y)])
        checked_map[x][y] = True
        answer_tmp = 1

        while bfs:
            x_tmp, y_tmp = bfs.popleft()

            tmp = [(max(0, x_tmp-1), y_tmp),
                   (min(x_tmp+1, N-1), y_tmp),
                   (x_tmp, max(0, y_tmp-1)),
                   (x_tmp, min(y_tmp+1, N-1))
                   ]

            for x_tmp2, y_tmp2 in tmp:
                if home_map[x_tmp2][y_tmp2] == "1" and not checked_map[x_tmp2][y_tmp2]:
                    checked_map[x_tmp2][y_tmp2] = True
                    bfs.append((x_tmp2, y_tmp2))
                    answer_tmp += 1

        answer.append(answer_tmp)

answer.sort()
print(len(answer))
for a in answer:
    stdout.write(str(a)+"\n")
