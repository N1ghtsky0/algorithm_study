num = [0] * 9
room = input().replace('9', '6')
for n in room: num[int(n)] += 1
num[6] = num[6]//2 + num[6] % 2
print(max(num))