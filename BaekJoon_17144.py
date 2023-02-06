# Baekjoon 17144
# https://www.acmicpc.net/problem/17144

from sys import stdin

def spread(m):
    m_ = [[0] * C for _ in " " * R]
    for r in range(R):
        for c in range(C):
            if m[r][c]: # 미세먼지가 있는 칸일 경우
                m_[r][c] += m[r][c]
                amount = m[r][c] // 5
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in air_cleaner:
                        m_[nr][nc] += amount
                        m_[r][c] -= amount
    return m_

def work():
    # 위쪽 공기청정기
    pre = 0
    r, c = r_, c_ = air_cleaner[0][0], 0
    for dist in range(2 * C + 2 * r - 3):
        if dist < C - 1: c_ += 1
        elif dist < C + r - 1: r_ -= 1
        elif dist < 2 * C + r - 2: c_ -= 1
        else: r_ += 1
        MAP[r_][c_], pre = pre, MAP[r_][c_]

    # 아래쪽 공기청정기
    pre = 0
    r, c = r_, c_ = air_cleaner[1][0], 0
    r = R - 1 - r
    for dist in range(2 * C + 2 * r - 3):
        if dist < C - 1: c_ += 1
        elif dist < C + r - 1: r_ += 1
        elif dist < 2 * C + r - 2: c_ -= 1
        else: r_ -= 1
        MAP[r_][c_], pre = pre, MAP[r_][c_]

rd = stdin.readline
R, C, T = map(int, rd().split())
MAP = [[*map(int, rd().split())] for _ in " " * R]

air_cleaner = []
for r in range(R):
    if MAP[r][0] == -1:
        MAP[r][0] = 0
        MAP[r + 1][0] = 0
        air_cleaner.append((r, 0))
        air_cleaner.append((r + 1, 0))
        break

for _ in " " * T:
    MAP = spread(MAP)
    work()

print(sum([sum(row) for row in MAP]))
