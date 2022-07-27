# BaekJoon 9012
# https://www.acmicpc.net/problem/9012

for _ in range(int(input())):
    result = []; result_str = 'YES'; tmp = 0
    for n in input():
        if n == '(': 
            result.append(n)
            tmp += 1
        else:
            tmp -= 1
            try:
                result.pop()
            except:
                result_str = 'NO'
                break
    if tmp != 0: result_str = 'NO'
    print(result_str)
