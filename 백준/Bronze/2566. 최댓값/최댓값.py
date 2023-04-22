from sys import stdin; input=stdin.readline
nums = []
for _ in range(9):
    nums += list(map(int, input().split()))
t = max(nums)
print(t)
idx = nums.index(t)
print(idx//9+1, idx%9+1)