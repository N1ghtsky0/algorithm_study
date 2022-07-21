# BaekJoon 1018
# https://www.acmicpc.net/problem/1018

import sys
target1 = 'BWBWBWBWWBWBWBWB'*4
target2 = 'WBWBWBWBBWBWBWBW'*4
h, w = map(int, input().split())
board = [sys.stdin.readline() for _ in range(h)]
result = 65
for row in range(w-7):
    for col in range(h-7):
        tmp = ''.join([board[i + col][row:row+8] for i in range(8)])
        bs, ws = 0, 0
        for i, (t1, t2) in enumerate(zip(target1, target2)):
            if tmp[i] != t1: bs += 1
            if tmp[i] != t2: ws += 1
        result = min(result, bs, ws)
print(result)
