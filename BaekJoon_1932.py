# Baekjoon 1932
# https://www.acmicpc.net/problem/1932

from sys import stdin; s_input = stdin.readline
n = int(input())
nums = [list(map(int, s_input().rstrip().split())) for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(len(nums[i])):
        nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])
print(nums[0][0])
