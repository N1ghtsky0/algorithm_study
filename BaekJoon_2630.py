# BaekJoon 2630
# https://www.acmicpc.net/problem/2630

from sys import stdin; input=stdin.readline
N = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(N)]
white, blue = 0, 0
def solution(x, y, n):
    global white, blue

    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n//2)
                solution(x, y + n//2, n//2)
                solution(x + n//2, y, n//2)
                solution(x + n//2, y + n//2, n//2)
                return
    if color: blue += 1
    else: white += 1
    return

solution(0, 0, N)
print(white)
print(blue)
