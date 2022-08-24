# BaekJoon 1992
# https://www.acmicpc.net/problem/1992

from sys import stdin; input=stdin.readline
N = int(input().strip())
video = [list(map(int, input().strip())) for _ in range(N)]
def solution(x, y, n):
    color = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != video[i][j]:
                print('(', end='')
                solution(x, y, n//2)
                solution(x, y + n//2, n//2)
                solution(x + n//2, y, n//2)
                solution(x + n//2, y + n//2, n//2)
                print(')', end='')
                return
    print(color, end='')

solution(0, 0, N)
