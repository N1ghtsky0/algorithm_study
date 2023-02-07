# baekjoon 1238
# https://www.acmicpc.net/problem/1238

import sys
from heapq import heappush, heappop

rd = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s):
    dist = [INF] * (N + 1)
    dist[0] = 0
    dist[s] = 0
    heap = []
    heappush(heap, (0, s))

    while heap:
        cur_dist, node = heappop(heap)

        if dist[node] < cur_dist:
            continue

        for next_node, next_dist in costs[node]:
            dist_ = cur_dist + next_dist
            if dist_ < dist[next_node]:
                dist[next_node] = dist_
                heappush(heap, (dist_, next_node))

    if s == X:
        for idx in range(N+1):
            ans[idx] += dist[idx]
    else:
        ans[s] += dist[X]

N, M, X = map(int, rd().split())
costs = [[] for _ in " " * (N + 1)]
for _ in " " * M:
    a, b, t = map(int, rd().split())
    costs[a].append((b, t))

ans = [0] * (N + 1)
for i in range(1, N+1):
    dijkstra(i)
print(max(ans))
