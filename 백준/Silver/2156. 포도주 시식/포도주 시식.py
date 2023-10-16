n = int(input())
wines = [int(input()) for _ in ' ' * n]
dp = [0, 0, 0]
for wine in wines:
    dp = [dp[2] + wine, dp[0] + wine, max(dp)]
print(max(dp))