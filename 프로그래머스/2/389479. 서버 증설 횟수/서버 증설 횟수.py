from collections import deque
def solution(players, m, k):
    answer = 0
    servers = deque([0] * k)
    for player in players:
        servers.rotate(-1); servers[-1] = 0
        need_new_server = True
        new_server = 0
        if (m > player) or (sum(servers) * m > player): need_new_server = False
        if (need_new_server):
            new_server = (player - sum(servers) * m) // m
        answer += new_server
        servers[-1] = new_server
    return answer