# BaekJoon 11726
# https://www.acmicpc.net/problem/11726

R = {1:1, 2:2, 3:3}
def s(n):
    if n in R: return R[n]
    else:
        R[n] = s(n-1) + s(n-2)
        return R[n]

print(s(int(input()))%10007)
