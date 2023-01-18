# Baekjoon 4963
# https://www.acmicpc.net/problem/4963

from sys import stdin

rd = stdin.readline

def bfs(r, c):
    global w, h
    bfs_lst = [(r, c)]

    while bfs_lst:
        x, y = bfs_lst.pop()

        tmp = [(x+dx, y+dy) for dy in [-1, 0, 1] for dx in [-1, 0, 1]]

        for nx, ny in tmp:
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                if m[nx][ny]:
                    bfs_lst.append((nx, ny))

while True:
    w, h = map(int, rd().split())

    if w == 0 and h == 0:
        break

    m = [list(map(int, rd().split())) for _ in " " * h]   # MAP
    visited = [[False] * w for _ in " " * h]
    answer = 0

    for i in range(w):
        for j in range(h):
            if visited[j][i]:
                continue

            visited[j][i] = True
            if m[j][i]:
                bfs(j, i)
                answer += 1
    print(answer)
