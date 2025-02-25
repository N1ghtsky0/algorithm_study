def solution(sticker):
    if len(sticker) < 3: return max(sticker)
    dp1 = [0 for _ in range(len(sticker) - 1)]
    dp1[0] = sticker[0]; dp1[1] = sticker[0]
    for idx in range(2, len(sticker) - 1):
        dp1[idx] = max(dp1[idx - 1], dp1[idx - 2] + sticker[idx])
    
    dp2 = [0 for _ in range(len(sticker))]
    dp2[0] = 0; dp2[1] = sticker[1]
    for idx in range(2, len(sticker)):
        dp2[idx] = max(dp2[idx - 1], dp2[idx - 2] + sticker[idx])
    return max(dp1[-1], dp2[-1])
        
    
        
