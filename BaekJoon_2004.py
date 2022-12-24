# Baekjoon 2004
# https://www.acmicpc.net/problem/2004

n, m = map(int, input().split())

lst = [0, 0]
i = 2
j = 5
while i <= n:
    lst[0] += n // i - m // i - (n-m) // i
    lst[1] += n // j - m // j - (n - m) // j
    i *= 2
    j *= 5

print(min(lst))
