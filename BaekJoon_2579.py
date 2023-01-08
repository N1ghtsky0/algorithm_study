# Baekjoon 2579
# https://www.acmicpc.net/problem/2579

from sys import stdin
input=stdin.readline
N = int(input())
scores = [int(input()) for _ in " " * N]

if N <= 2:
    print(sum(scores))
else:
    dp = [[-1, -1] for _ in " " * N]
    dp[0][0] = scores[0]
    dp[1][0] = scores[1]
    dp[1][1] = dp[0][0] + scores[1]

    for i in range(2, N):
        tmp = max(dp[i-2])
        if tmp > -1:
            dp[i][0] = tmp + scores[i]
        if dp[i-1][0] > -1:
            dp[i][1] = dp[i-1][0] + scores[i]

    print(max(dp[N-1]))
