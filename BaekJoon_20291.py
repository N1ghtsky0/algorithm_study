# BaekJoon 20291
# https://www.acmicpc.net/problem/20291

from sys import stdin; input=stdin.readline
f = {}
for _ in range(int(input().strip())):
    ex = input().split('.')[1]
    if ex in f: f[ex] += 1
    else: f[ex] = 1
for k in sorted(f.keys()):
    print(k.strip()+' '+str(f[k]))
