# BaekJoon 2447
# https://www.acmicpc.net/problem/2447

def solution(n):
    if n == 1:
        return ['*']
    
    s = solution(n//3)
    result = []

    for item in s:
        result.append(item*3)
    for item in s:
        result.append(item + ' ' * (n//3) + item)
    for item in s:
        result.append(item*3)
    return result

print('\n'.join(solution(int(input()))))  
