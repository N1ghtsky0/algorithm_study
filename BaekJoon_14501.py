# Baekjoon 14501
# https://www.acmicpc.net/problem/14501

def dfs(day, salary):
    global T, answer

    for blank, (period, money) in enumerate(period_and_money[day:]):
        if day + period + blank <= T+1:
            answer = max(answer, salary + money)
            dfs(day + period + blank, salary + money)

T = int(input())
period_and_money = [tuple([1, 0])] + [tuple(map(int, input().split())) for _ in range(T)]   # (period, money)
answer = 0
for i in range(T):
    dfs(period_and_money[i][0] + i, period_and_money[i][1])
print(answer)
