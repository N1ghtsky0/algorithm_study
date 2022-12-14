# Baekjoon 9095
# https://www.acmicpc.net/problem/9095

from collections import deque

for _ in range(int(input())):
    dp = deque([0])
    ans = 0
    n = int(input())
    while dp:
        num = dp.popleft()
        for i in [1, 2, 3]:
            if num + i <= n:
                if num + i == n: ans += 1
                else: dp.append(num + i)
    print(ans)
