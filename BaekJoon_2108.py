# BaekJoon 2108
# https://www.acmicpc.net/problem/2108

from sys import stdin
from collections import Counter

s = stdin.readline
num = [int(s().rstrip()) for _ in range(int(input()))]
num.sort()
num_count = {}

for k, v in Counter(num).items():
    if v in num_count.keys(): num_count[v].append(k)
    else: num_count[v] = [k]

# print mean
print(round(sum(num)/len(num))) 

# print median
print(num[len(num)//2])

# print mode
result = max(num_count.keys())

# When there are several, the second smallest of the lowest values is output.
if len(num_count[result]) != 1: print(num_count[result][1])
else: print(num_count[result][0])
  
#print range
print(num[-1]-num[0])
