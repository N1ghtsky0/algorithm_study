from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
_, *know_truth = map(int, input().split())
truth_party = [True] + [False for _ in range(M)]
queue = deque()

party_people = {party: [] for party in range(1, M + 1)}
people_party = {people: [] for people in range(1, N + 1)}
for m in range(1, M + 1):
    is_truth_party = False
    _, *participants = map(int, input().split())
    party_people[m] = participants
    for participant in participants:
        people_party[participant].append(m)
        if participant in know_truth:
            is_truth_party = True
    if is_truth_party:
        truth_party[m] = True
        queue.append(m)

while queue:
    party = queue.popleft()
    for people in party_people[party]:
        for another_party in people_party[people]:
            if not truth_party[another_party]:
                truth_party[another_party] = True
                queue.append(another_party)

print(truth_party.count(False))