# baekjoon 1012
# https://www.acmicpc.net/problem/1012

from collections import deque
from sys import stdin
input=stdin.readline

T = int(input())
for _ in range(T):
    answer = 0
    M, N, K = map(int, input().split())
    visited = {tuple(map(int, input().split())): False for _ in ' ' * K}

    for start in visited.keys():
        if visited[start]:
            continue
        else:
            bfs = deque([start])
            while bfs:
                state = bfs.popleft()
                tmp = {(state[0], max(0, state[1] - 1)),
                       (state[0], min(N, state[1] + 1)),
                       (min(M, state[0] + 1), state[1]),
                       (max(0, state[0] - 1), state[1])}

                for t in tmp:
                    if t in visited and not visited[t]:
                        bfs.append(t)
                        visited[t] = True
            answer += 1
    print(answer)
