# BaekJoon 11866
# https://www.acmicpc.net/problem/11866

N, K = map(int,input().split())
player = list(range(1, N+1))
result = []
for n in range(N):
    for _ in range(K-1):
        player = player[1:]+[player[0]]
    result.append(str(player[0]))
    player = player[1:]
print(f'<{", ".join(result)}>')
