# BaekJoon 1780
# https://www.acmicpc.net/problem/1780

from sys import stdin; input=stdin.readline
N = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(N)]
nums = [0,0,0]
def solution(x, y, n):
    global paper

    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n//3)
                solution(x, y + n//3, n//3)
                solution(x, y + n//3 * 2, n//3)

                solution(x + n//3, y, n//3)
                solution(x + n//3, y + n//3, n//3)
                solution(x + n//3, y + n//3 * 2, n//3)

                solution(x + n//3 * 2, y, n//3)
                solution(x + n//3 * 2, y + n//3, n//3)
                solution(x + n//3 * 2, y + n//3 * 2, n//3)
                return
    nums[color+1] += 1

solution(0, 0, N)
for i in nums: print(i)
