# Baekjoon 9663
# https://www.acmicpc.net/problem/9663

answer = 0

def solution(n, board, col):
    global answer

    if col == n:
        answer += 1
        return

    tmp = board.copy()
    for i in range(n):  # 현재 열(col)에서 퀸을 놓을 행(i)
        if col == 0:
            tmp[col] = i
            solution(n, tmp, col+1)
            continue

        next_step = True
        for j in range(col):    # 이전 열들을 살펴봄
            if (i in board) or (board[j] + (col - j) == i) or (board[j] - (col - j) == i):
                next_step = False
                break

        if next_step:
            tmp[col] = i
            solution(n, tmp, col+1)


N = int(input())
solution(N, [-100]*N, 0)
print(answer)
