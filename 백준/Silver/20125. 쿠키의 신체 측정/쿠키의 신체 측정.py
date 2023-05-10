def down(i, j):
    length = 1
    while i+1 < N and MAP[i+1][j] == '*':
        length += 1
        i += 1
    return length

N = int(input())
MAP = [input() for _ in ' ' * N]
ans = ""

x, y = 0, 0
for idx, line in enumerate(MAP):
    if len(set(line)) == 2:
        x = idx
        y = line.index("*")
        ans = str(x + 2) + " " + str(y + 1) + "\n"
        break

ans += str(y - MAP[x+1].index("*")) + " "
ans += str(MAP[x+1].rindex("*") - y) + " "
x_ = down(x, y)
ans += str(x_ - 2) + " "
ans += str(down(x + x_, y - 1)) + " "
ans += str(down(x + x_, y + 1))

print(ans)