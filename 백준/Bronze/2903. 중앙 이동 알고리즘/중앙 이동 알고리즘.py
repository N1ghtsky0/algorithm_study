p = 2
for _ in range(int(input())):
    p += p - 1
print(p ** 2)