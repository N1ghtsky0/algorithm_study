# Baekjoon 2193
# https://www.acmicpc.net/problem/status/2193

dp = {1: 1, 2: 1}

N = int(input())

for n in range(3, N+1):
    dp[n] = dp[n-2] + dp[n-1]

print(dp[N])
