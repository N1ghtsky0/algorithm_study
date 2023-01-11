# Baekjoon 10026
# https://www.acmicpc.net/problem/10026

from collections import deque
from sys import stdin

rd = stdin.readline


def BFS(board, i, j):
    target = board[i][j]
    bfs = deque([(i, j)])
    while bfs:
        x_current, y_current = bfs.popleft()

        tmp = [(max(0, x_current - 1), y_current),
               (min(x_current + 1, N - 1), y_current),
               (x_current, max(0, y_current - 1)),
               (x_current, min(y_current + 1, N - 1))
               ]

        for x_next, y_next in tmp:
            if board[x_next][y_next] == target and not visited[x_next][y_next]:
                bfs.append((x_next, y_next))
                visited[x_next][y_next] = True


N = int(rd())
img = [list(rd().rstrip()) for _ in " " * N]
visited = [[False] * N for _ in " " * N]

answer1 = 0
for r, line in enumerate(img):
    for c, color in enumerate(line):
        if not visited[r][c]:
            BFS(img, r, c)
            answer1 += 1

new_img = [list("".join(row).replace("R", "G")) for row in img]
visited = [[False] * N for _ in " " * N]

answer2 = 0
for r, line in enumerate(new_img):
    for c, color in enumerate(line):
        if not visited[r][c]:
            BFS(new_img, r, c)
            answer2 += 1

print(answer1, answer2)
