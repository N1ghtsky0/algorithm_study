# Baekjoon 11723 
# https://www.acmicpc.net/problem/11723

from sys import stdin; input = stdin.readline
S = [0]*21
for _ in range(int(input().strip())):
    command = input().split()
    if command[0] == 'add': S[int(command[1])] = 1
    elif command[0] == 'remove': S[int(command[1])] = 0
    elif command[0] == 'check': print(S[int(command[1])])
    elif command[0] == 'toggle': S[int(command[1])] = int(not S[int(command[1])])
    elif command[0] == 'all': S = [1]*21
    elif command[0] == 'empty': S = [0]*21
