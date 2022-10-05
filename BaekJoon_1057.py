# BaekJoon 1057
# https://www.acmicpc.net/problem/1057

N, num1, num2 = map(int, input().split())
answer = 0
while num1 != num2:
    num1 = (num1 + 1) // 2
    num2 = (num2 + 1) // 2
    answer += 1
print(answer)
