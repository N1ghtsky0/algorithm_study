# Baekjoon 11279
# https://www.acmicpc.net/problem/11279

import heapq

heap = []
for _ in range(int(input())):
    num = -1 * int(input())
    if num:
        heapq.heappush(heap, num)
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
