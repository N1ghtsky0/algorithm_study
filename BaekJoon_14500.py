# Baekjoon 14500
# https://www.acmicpc.net/problem/14500

from sys import stdin

rd = stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]   # up, down, right, left

N, M = map(int, rd().split())
board = [list(map(int, rd().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

maxValue = 0

def dfs(i, j, result, size):
    global maxValue

    if size == 4:
        maxValue = max(maxValue, result)
        return

    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, result + board[ni][nj], size+1)
            visited[ni][nj] = False


def exce(i, j):
    global maxValue

    for n in range(4):
        tmp = board[i][j]
        for k in range(3):
            # 012(ㅏ), 123(ㅜ), 230(ㅗ), 301(ㅓ)
            t = (n+k) % 4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                break
            tmp += board[ni][nj]

        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)
