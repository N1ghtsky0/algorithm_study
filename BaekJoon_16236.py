# Baekjoon 16236
# https://www.acmicpc.net/problem/16236

from sys import stdin
from collections import deque
import heapq

rd = stdin.readline

def bfs():
    global answer
    tmp = 0
    while q:
        tmp += 1
        next_steps = []
        step = len(q)
        for _ in " " * step:
            x, y = q.popleft()
            for mv_idx in range(4):
                nx, ny = x + dx[mv_idx], y + dy[mv_idx]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and space[nx][ny] <= shark_size: # 상어와 크기가 같거나 작은 물고기가 있는 칸으로만 이동 가능
                    if 0 < space[nx][ny] < shark_size:
                        next_steps.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
        heapq.heapify(next_steps)
        for nx, ny in next_steps:
            answer += tmp
            need_to_growth[shark_size] -= 1 # 한마리를 먹음
            fish_count[space[nx][ny]] -= 1
            space[shark_coord[0]][shark_coord[1]] = 0   # 원래 상어의 위치는 빈 칸으로 변경
            space[nx][ny] = 9   # 물고기를 먹은 위치로 상어 이동
            q.clear()   # 먹은 위치부터 bfs재시작 해야하기에 초기화 후 현재위치만 저장
            q.append((nx, ny))
            return [nx, ny]

dx = [-1, 0, 0, 1]  # 위, 왼쪽, 오른쪽, 아래
dy = [0, -1, 1, 0]
need_to_growth = [0, 0, 2, 3, 4, 5, 6, 400]
fish_count = [0] * 7
q = deque()

N = int(rd())
space = []
shark_coord = [0, 0]
for r in range(N):
    input_row = list(map(int, rd().split()))
    space.append(input_row)
    for c, v in enumerate(input_row):
        if v:
            if v == 9:
                q.append((r, c))
                shark_coord = [r, c]
            else:
                fish_count[v] += 1

answer = 0
shark_size = 2
while sum(fish_count[:shark_size]) and q: # 먹을 수 있는 물고기 (상어 크기보다 작은 물고기)가 존재하는 동안 계속 실행
    visited = [[False] * N for _ in " " * N]
    shark_coord = bfs() # 물고기를 먹을 수 있는 위치에 도달한 경우 bfs종료되므로 해당 위치로 상어의 좌표를 옮겨줌
    if not need_to_growth[shark_size]:
        shark_size += 1

print(answer)
