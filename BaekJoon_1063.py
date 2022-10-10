# BaekJoon 1063
# https://www.acmicpc.net/problem/1063

from sys import stdin; input=stdin.readline

def check_out(arr):
    # 체스판을 나가면 True, 아니면 False
    result = True if arr[0] < 1 or arr[0] > 8 or arr[1] < 1 or arr[1] > 8 else False
    return int(result)

def moving(command, arr):
    # Arr[0] : 행 A~H, Arr[1]: 열 1~8
    # RL : 행 이동, TB : 열 이동
    result = arr.copy()
    if command == 'R': result[0] += 1
    elif command == 'L': result[0] -= 1
    elif command == 'T': result[1] += 1
    elif command == 'B': result[1] -= 1
    elif command == 'RT': result[0] += 1; result[1] += 1
    elif command == 'LT': result[0] -= 1; result[1] += 1
    elif command == 'RB': result[0] += 1; result[1] -= 1
    elif command == 'LB': result[0] -= 1; result[1] -= 1

    return result

king, stone, move_count = input().split()
COORD = '_ABCDEFGH'
king_arr = [COORD.index(king[0]), int(king[1])]
stone_arr = [COORD.index(stone[0]), int(stone[1])]

for _ in range(int(move_count)):
    command = input().strip()
    new_king_arr = moving(command, king_arr.copy())

    new_stone_arr = stone_arr.copy()
    if new_king_arr == new_stone_arr:
        new_stone_arr = moving(command, stone_arr)
    
    is_out = check_out(new_king_arr) + check_out(new_stone_arr)

    if not is_out: # 이동 후 좌표들이 체스판을 벗어나지 않았을 경우
        king_arr = new_king_arr
        stone_arr = new_stone_arr

print(COORD[king_arr[0]]+str(king_arr[1]))
print(COORD[stone_arr[0]]+str(stone_arr[1]))
