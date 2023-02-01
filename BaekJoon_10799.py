# Baekjoon 10799
# https://www.acmicpc.net/problem/10799

n = input().replace("()", "*")
answer = tmp = 0
for s in n:
    if s == "*":
        answer += tmp
    if s == "(":
        tmp += 1
    elif s == ")":
        tmp -= 1
        answer += 1
print(answer)
