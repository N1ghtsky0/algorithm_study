# Baekjoon 9019
# https://www.acmicpc.net/problem/9019

from collections import deque
from sys import stdin

rd = stdin.readline

for _ in range(int(rd())):
    A, B = map(int, rd().split())
    q = deque()
    q.append((A, ""))
    visit = [False] * 10000

    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break

        # D
        num2 = (2 * num) % 10000
        if not visit[num2]:
            q.append((num2, path + "D"))
            visit[num2] = True

        # S
        num2 = (num - 1) % 10000
        if not visit[num2]:
            q.append((num2, path + "S"))
            visit[num2] = True

        # L
        num2 = num % 1000 * 10 + num // 1000
        if not visit[num2]:
            q.append((num2, path + "L"))
            visit[num2] = True

        # R
        num2 = num % 10 * 1000 + num // 10
        if not visit[num2]:
            q.append((num2, path + "R"))
            visit[num2] = True
