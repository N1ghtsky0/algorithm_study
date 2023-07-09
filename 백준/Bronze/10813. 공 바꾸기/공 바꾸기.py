N, M = map(int, input().split())

a = list(range(1, N+1))

for _ in ' ' * M:
    i, j = map(int, input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]

print(' '.join(map(str, a)))