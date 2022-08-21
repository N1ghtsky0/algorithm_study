# BaekJoon 17298
# https://www.acmicpc.net/problem/17298

N, A = int(input()), list(map(int, input().split()))
result = ['-1'] * N
stack = [0]

for idx in range(1, N):
    while stack and A[stack[-1]] < A[idx]:
        result[stack.pop()] = str(A[idx])
    stack.append(idx)
print(' '.join(result))
