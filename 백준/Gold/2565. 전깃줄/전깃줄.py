N = int(input())
cnt = 0
line = [() for _ in range(N)]
dp = [1 for _ in range(N)]
for i in range(N):
    s, e = map(int, input().split())
    line[i] = (s, e)

line.sort()

for i in range(N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
