N, K = map(int, input().split())
result = 0
for n in range(1, N+1):
    if N % n == 0: K -= 1
    if K == 0:
        result = n
        break
print(result)