from collections import deque

def init(M:int, N:int, K:int):
    board = [[False for _ in ' ' * N] for _ in ' ' * M]
    for _ in ' ' * K:
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                board[y][x] = True
    return board


def main():
    M, N, K = map(int, input().split())
    board = init(M, N, K)
    area = list()
    for row in range(M):
        for col in range(N):
            if not board[row][col]:
                _area = 1
                dq = deque()
                dq.append((row, col))
                board[row][col] = True
                while dq:
                    y, x = dq.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= x + dx < N and 0 <= y + dy < M and not board[y + dy][x + dx]:
                            dq.append((y + dy, x + dx))
                            board[y + dy][x + dx] = True
                            _area += 1
                area.append(_area)
    print(len(area))
    print(' '.join(map(str, sorted(area))))


if __name__ == '__main__':
    main()
