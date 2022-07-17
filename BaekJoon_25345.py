# BaekJoon 25345
# https://www.acmicpc.net/problem/25345

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nCr(n, r):
    f = factorial
    return int(f(n) // (f(r) * f(n - r)))

N, K = map(int, input().split())

print((nCr(N, K) * 2 ** (K - 1))%(10**9 + 7))
