# BaekJoon 9020
# https://www.acmicpc.net/problem/9020

import sys
Prime = [True] * 10001
for i in range(2, 101):
  if Prime[i]:
    for j in range(i+i, 10001, i): Prime[j] = False

T = int(input())
for _ in range(T):
  n = int(sys.stdin.readline().strip())
  n2 = int(n/2)
  while(1):
    if Prime[n2] and Prime[n-n2]:
      print(n2, n-n2)
      break
    n2 -= 1
