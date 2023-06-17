from sys import stdin

rd = stdin.readline


def up_down(m):
    return int(m)+1 if m-int(m) >= 0.5 else int(m)


n = sorted([int(rd()) for _ in ' ' * int(rd())])
if n:
    ex = up_down(len(n) * 0.15)
    n = n[ex:len(n) - ex]
    print(up_down(sum(n) / len(n)))
else:
    print(0)
