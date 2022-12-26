# Baekjoon 1074
# https://www.acmicpc.net/problem/1074

def solution(n, row, col, state):
    if n == 1:
        print(int(state + 2 * row + col))
        return

    s = (n-1) // 2

    if row <= s:
        if col <= s:    # 제2사분면
            solution(n // 2, row, col, state + 0)
        else:           # 제1사분면
            solution(n // 2, row, col - n // 2, state + n // 2 * n // 2)
    else:
        if col <= s:    # 제3사분면
            solution(n // 2, row - n // 2, col, state + n // 2 * n // 2 * 2)
        else:           # 제4사분면
            solution(n // 2, row - n // 2, col - n // 2, state + n // 2 * n // 2 * 3)


N, r, c = map(int, input().split())
solution(2**N, r, c, 0)
