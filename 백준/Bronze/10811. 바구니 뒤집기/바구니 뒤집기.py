N, M = map(int, input().split())
baskets = list(range(0, N+2))
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i:j+1] = reversed(baskets[i:j+1])
print(*baskets[1:N+1], sep=' ')