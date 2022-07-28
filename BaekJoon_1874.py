# BaekJoon 1874
# https://www.acmicpc.net/problem/1874

from sys import stdin
n = int(input())
targets = [int(stdin.readline().rstrip()) for _ in range(n)]
stk, R, result = [], [], []
i = 1; idx = 0
while True:
    if i == n + 1:
        if not stk: break
        elif targets[idx] != stk[-1]: break

    if stk == []:
        stk.append(i)
        result.append('+')
        i += 1
    if targets[idx] == stk[-1]:
        R.append(stk.pop())
        result.append('-')
        idx += 1
    else:
        stk.append(i)
        result.append('+')
        i += 1
if R == targets: print('\n'.join(result))
else: print('NO')
