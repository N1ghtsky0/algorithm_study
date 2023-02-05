# Baekjoon 15686
# https://www.acmicpc.net/problem/15686

from sys import stdin


def select_pos(pos: list[tuple], idx: int):  # 치킨집 M개를 고르는 함수
    if len(pos) == M:
        check_dist(pos)  # M개를 모두 골랐을 때 치킨 거리 계산
    else:
        idx_ = idx
        for p in chickens[idx + 1:]:  # 마지막 치킨집의 인덱스 + 1 부터 선정
            idx_ += 1
            pos.append(p)
            select_pos(pos, idx_)
            pos.pop()


def check_dist(pos: list[tuple]):
    global answer
    tmp = 0
    for h in houses:
        tmp_ = 1e9
        for p in pos:  # 모든 치킨집에 대해 해당 집과 거리가 가장 짧은 값을 계산
            tmp_ = min(tmp_, abs(h[0] - p[0]) + abs(h[1] - p[1]))
        tmp += tmp_
        if tmp >= answer:  # 거리 계산 도중 기존 정답값보다 클 경우 더 계산할 필요 X
            return
    answer = min(tmp, answer)


rd = stdin.readline
houses = []
chickens = []
answer = 1e9

N, M = map(int, rd().split())
for row in range(N):
    input_row = [*map(int, rd().split())]
    for col, value in enumerate(input_row):
        if value == 1:
            houses.append((row, col))
        elif value == 2:
            chickens.append((row, col))

select_pos([], -1)
print(answer)
