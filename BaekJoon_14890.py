# Baekjoon 14890
# https://www.acmicpc.net/problem/14890

from sys import stdin

def solution(line):
    checked = [False] * N
    for idx, h in enumerate(line):
        if idx == 0:
            continue
        if h != line[idx - 1]:
            if abs(h - line[idx - 1]) > 1: # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
                return False
            if line[idx - 1] < h:
                for l in range(L):
                    if idx-l-1 < 0: # 경사로를 놓다가 범위를 벗어나는 경우
                        return False
                    if checked[idx-l-1]:    # 경사로를 놓은 곳에 또 경사로를 놓는 경우
                        return False
                    if line[idx-l-1] != h - 1:  # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                        return False
                    checked[idx - l - 1] = True
            elif line[idx - 1] > h:
                for l in range(L):
                    try:
                        checked[idx + l] = True
                    except: # 경사로를 놓다가 범위를 벗어나는 경우
                        return False
                    if line[idx+l] != h:  # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                        return False
    return True

rd = stdin.readline
N, L = map(int, rd().split())
MAP = [[*map(int, rd().split())] for _ in " " * N]
answer = 0

for line in MAP:
    if solution(line):
        answer += 1

for line in zip(*MAP):
    if solution(line):
        answer += 1
print(answer)
