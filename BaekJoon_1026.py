# BaekJoon 1026
# https://www.acmicpc.net/problem/1026

input()
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
result = sum([a*b for a, b in zip(A, B)])
print(result)
