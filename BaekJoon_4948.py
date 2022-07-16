# BaekJoon 4948
# https://www.acmicpc.net/problem/4948

import sys
while (1):
  n = int(sys.stdin.readline())
  if n == 0: break
  n *= 2
  isPrime = [True]*(n+1)
  for i in range(2, int(n**0.5)+1):
    if isPrime[i]:
      for j in range(i+i, n+1, i): isPrime[j] = False
  de = [k for k in range(int(n/2)+1, n+1) if isPrime[k]]
  print(len(de))
