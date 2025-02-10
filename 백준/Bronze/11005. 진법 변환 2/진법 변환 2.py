N, B = map(int, input().split())
formation = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ""
while N >= B:
    result = formation[N % B] + result
    N //= B
result = formation[N % B] + result
print(result)