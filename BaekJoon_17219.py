# Baekjoon 17219
# https://www.acmicpc.net/problem/17219

from sys import stdin, stdout
rd = stdin.readline

N, M = map(int, rd().split())
domain_pw = {}
for _ in " " * N:
    info = rd().split()
    domain_pw[info[0]] = info[1]

stdout.write("\n".join([domain_pw[rd().rstrip()] for _ in " " * M]))
