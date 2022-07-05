# BackJoon 10828
# https://www.acmicpc.net/problem/10828

from sys import stdin
s = stdin.readline
stack = []
for _ in range(int(input())):
    item = s().rstrip().split()
    if item[0] == 'push': stack.append(item[1])
    elif item[0] == 'top':
        print(stack[-1]) if stack != [] else print(-1)
    elif item[0] == 'size':
        print(len(stack))
    elif item[0] == 'empty':
        print(0) if stack != [] else print(1)
    elif item[0] == 'pop':
        if stack == []: print(-1)
        else:
            print(stack[-1])
            stack = stack[:-1]
