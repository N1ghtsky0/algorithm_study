# BaekJoon 14889
# https://www.acmicpc.net/problem/14889

from sys import stdin
s = stdin.readline
N = int(input())
people = list(range(1, N+1))
synergy = [list(map(int, s().rstrip().split())) for _ in range(N)]
R = []
# S_ij + S_ji의 총합을 구하는 함수
def score(team):
    result = 0
    for i in team:
        for j in team:
            if i == j: continue
            result += synergy[i-1][j-1]
    return result

# N명일 때 팀을 구성할 수 있는 경우의 수를 구하는 함수
def team_building(team_lst):
    if len(team_lst[0]) == N//2:
        R.append(sorted(team_lst[0]))
        return

    lst = team_lst.copy()

    for p in people:
        for t in lst:
            t_cp = t.copy()
            if p not in t and p > t[-1]:
                t_cp.append(p)
                team_building([t_cp])

team_building([[i] for i in people])
R.sort()
diff = []
# 팀 경우의 수를 정렬했을 때 절반을 기준으로 앞 뒤가 같기 때문에 앞 부분만 확인
for r in range(len(R)//2):
    team2 = list(set(people) - set(R[r]))
    diff.append(abs(score(R[r]) - score(team2)))
print(min(diff))
