# Baekjoon 1068
# https://www.acmicpc.net/problem/1068

N = int(input())
tree = [[] for _ in " " * N]
parents = input()
deleted_node = int(input())

root = 0
for idx, parent in enumerate(map(int, parents.split())):
    if parent == -1:
        root = idx
        continue
    if idx == deleted_node or parent == deleted_node:
        continue
    tree[parent].append(idx)

dfs = [root]
answer = 0
while dfs:
    node = dfs.pop()
    if node == deleted_node:
        continue
    next_nodes = tree[node]

    if next_nodes:
        dfs += next_nodes
    else:
        answer += 1

print(answer)
