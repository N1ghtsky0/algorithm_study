# BaekJoon 24523
# https://www.acmicpc.net/problem/24523

T = int(input())
num = list(map(int, input().split()))
num_count = 1; num_idx = []
for i in range(1, T):
    if num[i-1] != num[i]:
        num_idx.append([i+1, num_count])
        num_count = 1
    else:
        num_count += 1
num_idx.append([-1, num_count])
for item in num_idx:
    print((str(item[0])+' ')*item[1], end='')
