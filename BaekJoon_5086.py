# BaekJoon 5086
# https://www.acmicpc.net/problem/5086

from sys import stdin

while True:
    a, b = map(int, stdin.readline().rstrip().split())
    if a == 0 and b == 0: break
    if a % b == 0: print('multiple')
    elif b % a == 0: print('factor')
    else: print('neither')
