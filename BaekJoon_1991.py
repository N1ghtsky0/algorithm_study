# Baekjoon 1991
# https://www.acmicpc.net/problem/1991

from sys import stdin

def search_child(p):
    for child in nodes[p]:
        if not child == ".":
            stack.append(child)

rd = stdin.readline
N = int(rd())
nodes = {}

for _ in range(N):
    parent, left, right = rd().split()
    nodes[parent] = [right, left]

answer_front = ""
answer_middle = ""
answer_back = ""

# 전위 순회, 일반적인 dfs
stack = ["A"]
while stack:
    p = stack.pop()
    answer_front += p
    search_child(p)
print(answer_front)

# 중위 순회, 오른쪽 자식은 부모 노드의 앞, 왼쪽 자식은 부모 노드의 뒤에 저장하여 왼쪽 > 노드 > 오른쪽 순으로 탐색
stack = ["A"]
visited = [False] * 26
while stack:
    p = stack.pop()
    if p == ".":
        continue
    if not visited[ord(p) - 65]:
        visited[ord(p) - 65] = True
        r, l = nodes[p]
        stack.extend([r, p, l])
    else:
        answer_middle += p
print(answer_middle)

# 후위 순회, visited를 선언하여 이미 방문한 노드의 경우 바로 정답으로 더해주고 방문하지 않았으면 본인과 자식 노드를 추가
stack = ["A"]
visited = [False] * 26
while stack:
    p = stack.pop()
    if not visited[ord(p) - 65]:
        visited[ord(p) - 65] = True
        stack.append(p)
        search_child(p)
    else:
        answer_back += p
print(answer_back)
