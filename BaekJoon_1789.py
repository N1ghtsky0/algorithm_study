# Baekjoon 1789
# https://www.acmicpc.net/problem/1789

S = int(input())

N = 1
S_sum = 0
while S_sum <= S:
    S_sum += N
    N += 1
print(N-2) 
