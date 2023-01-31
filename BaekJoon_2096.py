# Baekjoon 2096
# https://www.acmicpc.net/problem/2096

from sys import stdin

rd = stdin.readline
N = int(rd())
dp = [[[0, 0], [0, 0], [0, 0]]]
for _ in " " * N:
    a, b, c = map(int, rd().split())
    dp.append([[a, a], [b, b], [c, c]]) # 입력 받은 행 추가

    dp[1][0][0] += max(dp[0][0][0], dp[0][1][0])    # 왼쪽으로 도착하는 최소값 계산
    dp[1][1][0] += max(dp[0][0][0], dp[0][1][0], dp[0][2][0])   # 가운데로 도착하는 최소값 계산
    dp[1][2][0] += max(dp[0][1][0], dp[0][2][0])    # 오른쪽으로 도착하는 최소값 계산

    dp[1][0][1] += min(dp[0][0][1], dp[0][1][1])    # 왼쪽으로 도착하는 최대값 계산
    dp[1][1][1] += min(dp[0][0][1], dp[0][1][1], dp[0][2][1])   # 가운데로 도착하는 최대값 계산
    dp[1][2][1] += min(dp[0][1][1], dp[0][2][1])    # 오른쪽으로 도착하는 최대값 계산

    dp.pop(0)   # 기존에 있던 행 삭제

for i, z in enumerate(zip(*dp[-1])):
    print(min(z) if i else max(z), end=" ")
