def solution(board, moves):
    answer = 0
    
    catch = []
    step = 0
    
    for move in moves:
        move -= 1
        for line in board:
            item = line[move]
            if item == 0: continue
            catch.append(item)
            line[move] = 0
            break
    
        if len(catch) >= 2:
            if catch[-1] == catch[-2]:
                del catch[-1]
                del catch[-1]
                answer += 1
    return answer * 2