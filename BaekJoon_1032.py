# Baekjoon 1032
# https://www.acmicpc.net/problem/1032

from sys import stdin; input=stdin.readline
files = [input().strip() for _ in range(int(input().strip()))]
answer = ''
for lst in zip(*files):
    answer += lst[0] if len(set(lst)) == 1 else '?'
print(answer)
