# Baekjoon 18111
# https://www.acmicpc.net/problem/18111

from collections import Counter
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = []
for _ in ' ' * N:
    blocks += list(map(int, input().split()))

info = Counter(blocks)
ans_time, ans_height = sys.maxsize, 0

for height in range(min(blocks), max(blocks) + 1):  # target : 만들려고하는 층 수
    break_block = 0
    need_block = 0
    for value in info:  # value : 블록의 층 수, info[value] : 해당 층에 해당하는 블록 수
        if value > height: break_block += (value - height) * info[value]
        else: need_block += (height - value) * info[value]

    if break_block + B >= need_block:
        if need_block + 2 * break_block <= ans_time:
            ans_time = need_block + 2 * break_block
            ans_height = height

print(ans_time, ans_height)
