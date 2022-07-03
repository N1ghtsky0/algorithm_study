# BaekJoon 25306
# https://www.acmicpc.net/problem/25306

A, B = map(int, input().split())

def xor(n):
    start = n//4 * 4
    answer = 0
    for i in range(start, n+1):
        answer ^= i
    return answer

print(xor(A-1) ^ xor(B))
