T = int(input())

dp = [0] * 11
dp[0] = 1

for i in range(1, 11):
    if i >= 1:
        dp[i] += dp[i - 1]
    if i >= 2:
        dp[i] += dp[i - 2]
    if i >= 3:
        dp[i] += dp[i - 3]

for i in range(T):
    n = int(input())  # n < 11
    result = dp[n]
    print(result)
