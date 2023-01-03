# Baekjoon 7662
# https://www.acmicpc.net/problem/7662

import heapq
from sys import stdin

input = stdin.readline

for T in range(int(input())):
    k = int(input())
    visited = [False] * k
    max_heap, min_heap = [], []
    for i in range(k):
        operation, n = input().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = True
        else:
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    print(-max_heap[0][0], min_heap[0][0]) if max_heap and min_heap else print("EMPTY")
