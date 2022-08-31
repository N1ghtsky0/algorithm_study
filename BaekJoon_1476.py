# BaekJoon 1476
# https://www.acmicpc.net/problem/1476

esm = list(map(int, input().split()))
answer = 1
while True:
    if esm == [1, 1, 1]: print(answer); break
    esm[0] = esm[0] - 1 if esm[0] - 1 > 0 else 15
    esm[1] = esm[1] - 1 if esm[1] - 1 > 0 else 28
    esm[2] = esm[2] - 1 if esm[2] - 1 > 0 else 19
    answer += 1
