# Baekjoon 1166
# https://www.acmicpc.net/problem/1166

N, L, W, H = map(int, input().split())
left = 0.0
right = min(L, W, H) * 1.0

for _ in " " * 10000:
    A = (left + right) / 2.0

    if ((L // A) * (W // A) * (H // A)) < N:
        right = A
    else:
        left = A

print(right)
