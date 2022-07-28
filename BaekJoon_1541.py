# BaekJoon 1541
# https://www.acmicpc.net/problem/1541

result, num = 0, ''
minus = False
for n in input() +' ':
    if n.isdigit(): num += n
    else:
        if minus: result -= int(num)
        else: result += int(num)
        if n == '-': minus = True
        num = ''
print(result)
