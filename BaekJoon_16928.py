# Baekjoon 16928
# https://www.acmicpc.net/problem/16928

from collections import deque

N, M = map(int, input().split())

ladders = {}
for _ in range(N):
    ls, le = map(int, input().split())
    ladders[ls] = le

snakes = {}
for _ in range(M):
    ss, se = map(int, input().split())
    ladders[ss] = se

visited = [False] * 101
answer = 0
bfs = deque([1])
done = False
while not done:
    repeat_num = len(bfs)
    for _ in " " * repeat_num:
        state = bfs.popleft()
        next_states = [state + i for i in range(1, 7)]
        for next_state in next_states:
            if next_state in ladders:
                next_state = ladders[next_state]
            elif next_state in snakes:
                next_state = snakes[next_state]

            if next_state >= 100:
                done = True
                break

            if not visited[next_state]:
                visited[next_state] = True
                bfs.append(next_state)

        if done:
            break
    answer += 1
print(answer)
