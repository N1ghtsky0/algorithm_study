from sys import stdin
from collections import deque

rd = stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dr = [0, 1, -1, -1, 1] # deque.rotate

dice = [deque([0, 0, 0, 0]),
        deque([0, 0, 0, 0])]

N, M, x, y, K = map(int, rd().split())

MAP = [list(map(int, rd().split())) for _ in ' ' * N]
commands = map(int, rd().split())

for command in commands:
    nx, ny = x + dx[command], y + dy[command]
    if 0 <= nx < N and 0 <= ny < M:
        x += dx[command]
        y += dy[command]

        dice[command//3].rotate(dr[command])   # 동, 서는 dice 0행, 남, 북은 dice 1행을 회전

        if command // 3:    # 밑면 동기화
            dice[0][1] = dice[1][1]
            dice[0][3] = dice[1][3]
        else:
            dice[1][1] = dice[0][1]
            dice[1][3] = dice[0][3]

        if MAP[x][y]:
            dice[0][-1] = dice[1][-1] = MAP[x][y]
            MAP[x][y] = 0
        else:
            MAP[x][y] = dice[0][-1]

        print(dice[0][1])