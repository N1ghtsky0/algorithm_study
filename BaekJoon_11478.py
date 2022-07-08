# BaekJoon 11478
# https://www.acmicpc.net/problem/11478

s = input()
n = len(s)
s_lst = sum(len({s[idx-num:idx] for idx in range(num, n + 1)}) for num in range(1, n + 1))
print(s_lst)
