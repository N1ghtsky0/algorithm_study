# BaekJoon 25239
# https://www.acmicpc.net/problem/25239

from sys import stdin
s = stdin.readline
 
def time_area(hh, mm):
    ang = hh * 15 + (mm * 25) * 0.01
    area = ang // 30
    return int(area)
 
hh, mm = map(int, input().split(':'))
heal = list(map(int, input().split()))
event = int(input())
 
for _ in range(event):
    s_T, command = map(str, s().rstrip().split())
    if command == '^': heal[time_area(hh, mm)] = 0
    elif command == '10MIN': hh, mm = (hh + (mm + 10) // 60) % 12, (mm + 10) % 60
    elif command == '30MIN': hh, mm = (hh + (mm + 30) // 60) % 12, (mm + 30) % 60
    elif command == '50MIN': hh, mm = (hh + (mm + 50) // 60) % 12, (mm + 50) % 60
    elif command == '2HOUR': hh = (hh + 2) % 12
    elif command == '4HOUR': hh = (hh + 4) % 12
    elif command == '9HOUR': hh = (hh + 9) % 12
 
print(min(sum(heal), 100))
