# BaekJoon 25286
# https://www.acmicpc.net/problem/25286

from sys import stdin

def leap_year(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)

days30 = [4, 6, 9, 11]

for _ in range(int(input())):
    result = []
    year, month = map(int, stdin.readline().rstrip().split())

    if month == 1: month = 13

    if month == 13: result.append(str(year-1))
    else: result.append(str(year))

    if month -1 == 2: result += ['2', str(28 + int(leap_year(year)))]
    elif month - 1 in days30: result += [str(month - 1), '30']
    else: result += [str(month - 1), '31']

    print(' '.join(result))
