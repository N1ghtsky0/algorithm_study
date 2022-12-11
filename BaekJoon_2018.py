# Baekjoon 2018
# https://www.acmicpc.net/problem/2018

def func(a, l):
    n = l - a + 1
    return int(n * (2 * a + (n - 1)) / 2)

N = int(input())
length = 2
done = False
ans = 1

for _ in ' '* (N//2):
    if done: break

    n = N // length
    for i in range(n, 0, -1):
        if func(i, i + length - 1) <= N:
            if func(i, i + length - 1) == N:
                ans += 1
            length += 1
            break
        if i == 1: done = True
print(ans)
