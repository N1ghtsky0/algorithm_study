# BaekJoon 1058
# https://www.acmicpc.net/problem/1058

from sys import stdin; input=stdin.readline
N = int(input().strip())
friends = {idx:[] for idx in range(N)}

for i in range(N):
    relation = input().strip()
    for j, f in enumerate(relation):
        if f == 'Y': friends[i].append(j)

result = 0
for key in friends.keys():
    tmp = set(friends[key].copy())
    for v in friends[key]:
        tmp |= set(friends[v])
    result = max(result, len(set(tmp))-1)
print(result)
