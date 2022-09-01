# BaekJoon 25501
# https://www.acmicpc.net/problem/25501

from sys import stdin; input=stdin.readline
def recursion(s, l, r):
    global c
    c += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    c = 0
    s = input().strip()
    print(f'{isPalindrome(s)} {c}')
