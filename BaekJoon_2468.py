# Baekjoon 2468
# https://www.acmicpc.net/problem/2468

from sys import stdin

rd = stdin.readline
N = int(rd())

heights = []
limits = set([])

for _ in " " * N:
    info = list(map(int, rd().split()))
    heights.append(info)
    limits |= set(info)

limits = sorted(list(limits))
answer = 1
for limit in limits:
    visited = [[False] * N for _ in " " * N]
    tmp_answer = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if heights[r][c] > limit:
                    dfs = [(r, c)]
                    while dfs:
                        cr, cc = dfs.pop()

                        tmp = [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]
                        for nr, nc in tmp:
                            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                                if heights[nr][nc] > limit:
                                    dfs.append((nr, nc))
                                visited[nr][nc] = True
                    tmp_answer += 1
            visited[r][c] = True
    answer = max(answer, tmp_answer)
print(answer)
