# Baekjoon 6064
# https://www.acmicpc.net/problem/6064

from sys import stdin, stdout

rd = stdin.readline
answer_lst = []
for _ in " " * int(rd()):
    M, N, x, y = map(int, rd().split())
    if x == y:
        answer_lst.append(str(x))
        continue

    interval, limit, start_point, target = (M, N, x, y) if M < N else (N, M, y, x)
    answer = tmp = start_point

    while True:
        tmp -= (limit - interval)
        tmp += limit if tmp <= 0 else 0

        answer += interval

        if tmp == target:
            break

        if tmp == start_point:
            answer = -1
            break

    answer_lst.append(str(answer))
stdout.write("\n".join(answer_lst))
