def solution(arr):
    answer = [0, 0]
    compression(0, 0, len(arr), arr, answer)
    return answer
    
def compression(row, col, n, arr, answer):
    target = arr[row][col]
    for dr in range(n):
        for dc in range(n):
            if arr[row + dr][col + dc] != target:
                compression(row, col, n//2, arr, answer)
                compression(row, col + n//2, n//2, arr, answer)
                compression(row + n//2, col, n//2, arr, answer)
                compression(row + n//2, col + n//2, n//2, arr, answer)
                return
    answer[target] += 1
    return