# Baekjoon 9251
# https://www.acmicpc.net/problem/9251

A = input()
B = input()
dp = [[0] * (len(A) + 1) for _ in " " * (len(B) + 1)]

for idx_b, b in enumerate(B, 1):
    for idx_a, a in enumerate(A, 1):
        if b == a:
            dp[idx_b][idx_a] = dp[idx_b - 1][idx_a - 1] + 1
        else:
            dp[idx_b][idx_a] = max(dp[idx_b - 1][idx_a], dp[idx_b][idx_a - 1])
print(dp[-1][-1])
