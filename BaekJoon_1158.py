# Baekjoon 1158
# https://www.acmicpc.net/problem/1158

from collections import deque

N, K = map(int, input().split())
nums = deque(range(1, N+1))
answer = ''

while nums:
    for _ in range(K-1):
        nums.append(nums.popleft())
    answer += str(nums.popleft()) + ', '

print(f'<{answer[:-2]}>')
