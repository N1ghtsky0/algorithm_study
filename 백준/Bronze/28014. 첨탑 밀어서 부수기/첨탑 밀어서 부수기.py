N = int(input())
spires = list(map(int, input().split()))
ans = 1
for i in range(1, N):
    if spires[i-1] <= spires[i]:
        ans += 1
print(ans)