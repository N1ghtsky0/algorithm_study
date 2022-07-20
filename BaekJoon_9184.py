# BaekJoon 9184
# https://www.acmicpc.net/problem/9184

from sys import stdin
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        if (a, b, c) not in answer:
            answer[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return answer[(a, b, c)] 
    else:
        if (a, b, c) not in answer:
            answer[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return answer[(a, b, c)]

answer = {}
while 1:    
    a, b, c = map(int, stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1: break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
