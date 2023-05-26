def dfs(idx, cnt, weight):
    global ans
    if cnt == N:
        ans += 1
        return

    if weight < 500:
        return

    for i in range(N):
        if not used[i]:
            weight += kit[i]
            used[i] = 1
            dfs(i, cnt+1, weight-K)
            weight -= kit[i]
            used[i] = 0


N, K = map(int, input().split())
kit = list(map(int, input().split()))
used = [0] * N
ans = 0
dfs(0, 0, 500)

print(ans)