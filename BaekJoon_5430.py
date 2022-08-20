# BaekJoon 5430
# https://www.acmicpc.net/problem/5430

from sys import stdin; input=stdin.readline
from collections import deque
for _ in range(int(input())):
    p, n = input().strip(), int(input().strip())
    x = input().strip()
    if p.count('D') > n: print('error'); continue
    elif n == 0 and p.count('D') == 0: print('[]'); continue
    x = deque(map(int, x[1:-1].split(',')))

    pop_direction = 1 # 1 : Leftpop, -1 : Rightpop
    for command in p:
        if command == 'R': pop_direction *= -1; continue
        if pop_direction + 1: x.popleft()
        else: x.pop()
    result = list(x)
    if pop_direction + 1: print(f'[{",".join([str(num) for num in result])}]')
    else: print(f'[{",".join([str(num) for num in result[::-1]])}]')
