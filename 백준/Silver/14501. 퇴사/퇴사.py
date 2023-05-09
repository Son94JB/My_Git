def sol(idx, money):
    global ans

    if idx > N:
        if idx > N+1:
            return
        ans = max(ans, money)
        return

    sol(idx+table[idx][0], money+table[idx][1])
    sol(idx+1, money)


N = int(input())
ans = 0
table = [() for _ in range(N+1)]
for i in range(N):
    t, p = map(int, input().split())
    table[i+1] = (t, p)

sol(1, 0)
print(ans)
