# Baekjoon 14502
# https://www.acmicpc.net/problem/14502

def make_2darr(arr, n, m):
    return [arr[s: s + m].copy() for s in range(0, n*m, m)]

def bfs(arr, visit, n, m):
    bfs_lst = virus.copy()
    arr2 = make_2darr(arr, n, m)

    while bfs_lst:
        r, c = bfs_lst.pop()
        next_rc = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for nr, nc in next_rc:
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc]:
                visit[nr][nc] = True
                if arr2[nr][nc] == "0":
                    arr2[nr][nc] = "2"
                    bfs_lst.append((nr, nc))
    safe_area(arr2)

def safe_area(arr):
    global answer
    tmp = 0
    for lst in arr:
        tmp += lst.count("0")
    answer = max(tmp, answer)

N, M = map(int, input().split())
lab = []
for _ in range(N):
    row = input().split()
    lab += row

virus = []
for idx, value in enumerate(lab):
    if value == "2":
        virus.append((idx // M, idx % M))

answer = 0
for i in range(N * M-2):
    if lab[i] == "0":
        lab[i] = "1"
        for j in range(i+1, N * M - 1):
            if lab[j] == "0":
                lab[j] = "1"
                for k in range(j + 1, N * M):
                    if lab[k] == "0":
                        lab[k] = "1"

                        visited = [[False] * M for _ in range(N)]
                        bfs(lab, visited, N, M)

                        lab[k] = "0"
                lab[j] = "0"
        lab[i] = "0"

print(answer)
