# Baekjoon 11054
# https://www.acmicpc.net/problem/11054

N = int(input())
A = [*map(int, input().split())]
A_ = A[::-1]
dp1 = [0] * N
dp2 = [0] * N
for current in range(N):
    for previous in range(current):
        if A[current] > A[previous] and dp1[current] < dp1[previous]:
            dp1[current] = dp1[previous]
        if A_[current] > A_[previous] and dp2[current] < dp2[previous]:
            dp2[current] = dp2[previous]
    dp1[current] += 1
    dp2[current] += 1

print(max([dp1[idx] + dp2[N - idx - 1] for idx in range(N)]) - 1)
