# BaekJoon 25593
# https://www.acmicpc.net/problem/25593

from sys import stdin; input=stdin.readline
work_man = {}
work_times = [4, 6, 4, 10]
weeks = int(input().strip())
for w in range(weeks):
    for t in range(4):
        work_time = work_times[t]
        for name in input().split():
            if name != '-':
                try: work_man[name] += work_time
                except: work_man[name] = work_time
value = work_man.values()
answer = 'Yes' if len(work_man) == 0 or max(value) - min(value) <= 12 else 'No'
print(answer)
