from sys import stdin
from collections import deque

rd = stdin.readline

N = int(input())
visited = [False] * (N + 1)
conn = dict()

conn[1] = []
visited[1] = True

for _ in ' ' * int(input()):
    a, b = map(int, rd().split())

    if a in conn.keys():
        conn[a].append(b)
    else:
        conn[a] = [b]

    if b in conn.keys():
        conn[b].append(a)
    else:
        conn[b] = [a]

Q = deque([1])
while Q:
    s = Q.popleft()
    for e in conn[s]:
        if not visited[e]:
            visited[e] = True
            Q.append(e)

print(sum(visited) - 1) # 1번을 통해 감염된 컴퓨터의 수 이므로 1번은 제외