# Baekjoon 1916
# https://www.acmicpc.net/problem/1916

from sys import stdin
import sys

def get_index():    # 방문하지 않은 노드들 중에 최단거리 인덱스 찾기
    value = INF
    index = 0
    for idx in range(1, N + 1):
        if not visited[idx] and answer[idx] < value:
            value = answer[idx]
            index = idx
    return index

def dijkstra(s):
    answer[s] = 0   # 시작노드 0으로 초기화
    visited[s] = True

    for next_node, cost in costs[s]:    # 시작노드와 인접한 노드들 초기화
        answer[next_node] = min(answer[next_node], cost)    # 같은 노선에 대한 값이 들어올 수도 있으므로 최소값만 저장

    for _ in " " * (N - 1):
        current = get_index()
        visited[current] = True
        for next_node, cost in costs[current]:
            cost += answer[current]
            answer[next_node] = min(answer[next_node], cost)

rd = stdin.readline
INF = sys.maxsize
N = int(rd())
M = int(rd())

costs = [[] for _ in " " * (N + 1)]
for _ in " " * M:
    s, e, c = map(int, rd().split())
    costs[s].append((e, c))

start, target = map(int, rd().split())
answer = [INF] * (N + 1)
visited = [False] * (N + 1)
dijkstra(start)

print(answer[target])
