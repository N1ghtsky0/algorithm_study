# Baekjoon 11403
# https://www.acmicpc.net/problem/11403

N = int(input())

G = [list(map(int, input().split())) for _ in " " * N]
answer = [["0"] * N for _ in " " * N]
connections = {idx: set([]) for idx in range(N)}

for r, row in enumerate(G):
    for c, col in enumerate(row):
        if col:
            connections[r].add(c)

for n in range(N):
    tmp = connections[n].copy()
    while tmp:
        node = tmp.pop()
        connections[n].add(node)
        answer[n][node] = "1"
        for new in connections[node]:
            if new not in connections[n]:
                tmp.add(new)

for a in answer:
    print(" ".join(a))
