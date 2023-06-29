from heapq import heappush, heappop
from sys import stdin

rd = stdin.readline
n = int(rd())

max_heap = []
min_heap = []
for i in range(n):
    num = int(rd())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    if min_heap and min_heap[0] < -max_heap[0]:
        leftValue = heappop(max_heap)
        rightValue = heappop(min_heap)

        heappush(max_heap, -rightValue)
        heappush(min_heap, -leftValue)

    print(-max_heap[0])