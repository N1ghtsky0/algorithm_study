def solution(park, routes):
    answer = []
    W, H = len(park[0]), len(park)
    for row, line in enumerate(park):
        if "S" in set(line):
            answer = [row, line.index("S")]
            break
            
    for route in routes:
        op, n = route.split()
        n = int(n)
        if op == "E":
            if (answer[1] + n >= W) or ("X" in park[answer[0]][answer[1] + 1 : answer[1] + n + 1]): continue
            answer[1] += n
        elif op == "W":
            if (answer[1] - n < 0) or ("X" in park[answer[0]][answer[1] - n : answer[1]]): continue
            answer[1] -= n
        elif op == "S":
            target = list(zip(*park))[answer[1]]
            if (answer[0] + n >= H) or ("X" in target[answer[0] + 1 : answer[0] + n + 1]): continue
            answer[0] += n
        else:
            target = list(zip(*park))[answer[1]]
            if (answer[0] - n < 0) or ("X" in target[answer[0] - n : answer[0]]): continue
            answer[0] -= n
    
    return answer