# BaekJoon 1966
# https://www.acmicpc.net/problem/1966

from sys import stdin; s_input = stdin.readline
for _ in range(int(input())):
    lst_len, t = map(int, s_input().rstrip().split())
    imp = list(map(int, s_input().rstrip().split()))
    idx, target, order = 0, max(imp), [False]*lst_len
    order[t] = True

    while 1:
        if imp[0] == target:
            idx += 1
            if order[0]:
                print(idx)
                break
            imp, order = imp[1:], order[1:]
            target = max(imp)
        else:
            imp, order = imp[1:] + [imp[0]] , order[1:] + [order[0]]
