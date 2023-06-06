def solution(word):
    answer = 1
    for c1 in ['A', 'E', 'I', 'O', 'U']:
        if (c1 == word): return answer
        else:
            answer += 1
            for c2 in ['A', 'E', 'I', 'O', 'U']:
                if (c1 + c2 == word): return answer
                else:
                    answer += 1
                    for c3 in ['A', 'E', 'I', 'O', 'U']:
                        if (c1 + c2 + c3 == word): return answer
                        else:
                            answer += 1
                            for c4 in ['A', 'E', 'I', 'O', 'U']:
                                if (c1 + c2 + c3 + c4 == word): return answer
                                else:
                                    answer += 1
                                    for c5 in ['A', 'E', 'I', 'O', 'U']:
                                        if (c1 + c2 + c3 + c4 + c5 == word): return answer
                                        else:
                                            answer += 1
    return answer