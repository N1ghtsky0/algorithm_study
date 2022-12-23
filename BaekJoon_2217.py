# Baekjoon 2217
# https://www.acmicpc.net/problem/2217

N = int(input())
print(max([l * k for k, l in enumerate(sorted([int(input()) for _ in ' ' * N], reverse=True), 1)]))
