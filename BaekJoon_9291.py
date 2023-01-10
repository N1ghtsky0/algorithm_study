# Baekjoon 9291
# https://www.acmicpc.net/problem/9291

from sys import stdin

rd = stdin.readline


def check_line(line):
    return len(set(line)) == 9


def check_square(board, r, c):
    square = [board[r+i][c+j] for i in [0, 1, 2] for j in [0, 1, 2]]
    return len(set(square)) == 9


T = int(rd())
for t in range(1, T+1):
    sudoku = [rd().split() for _ in range(9)]

    correct = True

    for row in sudoku:
        if not check_line(row):
            correct = False
            break

    if correct:
        for col in zip(*sudoku):
            if not check_line(col):
                correct = False
                break

    if correct:
        for n in range(0, 7, 3):
            for m in range(0, 7, 3):
                if not check_square(sudoku, n, m):
                    correct = False
                    break

            if not correct:
                break

    answer = "CORRECT" if correct else "INCORRECT"
    print(f"Case {t}: {answer}")

    if t < T:
        rd()
