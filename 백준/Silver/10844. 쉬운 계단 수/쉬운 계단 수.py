dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for n in range(1, int(input())):
    _dp = []
    for i in range(10):
        if i == 0: _dp.append(dp[1])
        elif i == 9: _dp.append(dp[8])
        else: _dp.append(dp[i-1] + dp[i+1])
    dp = _dp
print(sum(dp[1:]) % 1000000000)