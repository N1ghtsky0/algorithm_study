# BaekJoon 14888
# https://www.acmicpc.net/problem/14888

N = int(input()); A = list(map(int, input().split()))
Operator = list(map(int, input().split())) # [+, -, *, /]

def calculate(num1, num2, ope):
    if ope == 0: return num1 + num2
    elif ope == 1: return num1 - num2
    elif ope == 2: return num1 * num2
    else:
        if num1 < 0 and num2 > 0: return -1 * (-1 * num1 // num2)
        else: return num1 // num2

result = []

def solution(idx, num, ope):
    # 마지막 층에서 계산 결과 저장
    if idx == N - 1:
        for i, item in enumerate(ope):
            if item: 
                result.append(calculate(num, A[idx], i))
                return

    for i, item in enumerate(ope):
        tmp = ope.copy()
        if item:
            tmp[i] -= 1
            R = calculate(num, A[idx], i)
            solution(idx + 1, R, tmp)

solution(1, A[0], Operator)
print(max(result))
print(min(result))
