# Baekjoon 1987
# https://www.acmicpc.net/problem/1987

def dfs(x, y, hist):
    global answer
    for mv_idx in range(4):
        nx, ny = x + dx[mv_idx], y + dy[mv_idx]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            visited[nx][ny] = True
            if board[nx][ny] not in hist:
                hist_ = hist + board[nx][ny]
                answer = max(answer, len(hist_))
                dfs(nx, ny, hist_)
            visited[nx][ny] = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]
answer = 1
visited = [[False] * C for _ in range(R)]
visited[0][0] = True
dfs(0, 0, board[0][0])
print(answer)
