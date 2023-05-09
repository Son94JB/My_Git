N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]
r_dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
arr.reverse()
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            r_dp[i] = max(r_dp[i], r_dp[j]+1)

for i in range(N):
    dp[i] = dp[i] + r_dp[N - i - 1] - 1

print(max(dp))
