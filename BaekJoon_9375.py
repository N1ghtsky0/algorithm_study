# BaekJoon 9375
# https://www.acmicpc.net/problem/9375

from sys import stdin
s = stdin.readline
for _ in range(int(input())):
    clothes = {}
    for _ in range(int(input())):
        _, item = map(str, s().rstrip().split())
        if item in clothes: clothes[item] += 1
        else: clothes[item] = 1
    result = 1
    for key in clothes.keys():
        result *= (clothes[key] + 1)
    print(result - 1)
