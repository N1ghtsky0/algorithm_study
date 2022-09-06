# BaekJoon 1251
# https://www.acmicpc.net/problem/1251

def r(s):
    return s[::-1]

R = []
s = input()
for i1 in range(len(s)-2):
    for i2 in range(i1 + 1, len(s)-1):
        for i3 in range(i2 + 1, len(s)):
            R.append(r(s[:i1+1]) + r(s[i1+1:i3]) + r(s[i3:]))
print(sorted(list(set(R)))[0])
