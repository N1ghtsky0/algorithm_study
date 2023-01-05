# Baekjoon 2178
# https://www.acmicpc.net/problem/2178

from sys import stdin
from collections import deque
rd = stdin.readline

N, M = map(int, rd().split())

maze = [rd() for _ in " " * N]
visited = [[False] * M for _ in " " * N]

bfs = deque([[0, 0]])
visited[0][0] = True
done = False
answer = 1

while True:
    l = len(bfs)
    for _ in " " * l:
        s = bfs.popleft()

        tmp = [[s[0], max(0, s[1]-1)]
               , [s[0], min(M-1, s[1]+1)]
               , [max(0, s[0]-1), s[1]]
               , [min(N-1, s[0]+1), s[1]]
               ]

        for i, j in tmp:
            if maze[i][j] == "1" and not visited[i][j]:
                if i == N - 1 and j == M - 1:
                    done = True
                    break
                bfs.append([i, j])
                visited[i][j] = True
    answer += 1

    if done:
        print(answer)
        break
