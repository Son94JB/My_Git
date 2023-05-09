import sys
input = sys.stdin.readline


N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 2
for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

ans = dp[N-1] % 10007
print(ans)
