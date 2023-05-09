def sol(a, b):
    if a < 0 or b < 0:
        return True

    if a < arr[0] and b < arr[0]:
        return False

    if dp[a][b] != -1:
        return dp[a][b]

    cnt = 0

    for n in arr:
        if not sol(a - n, b):
            cnt += 1
        if not sol(a, b - n):
            cnt += 1

    if cnt:
        dp[a][b] = True
    else:
        dp[a][b] = False

    return dp[a][b]


arr = list(map(int, input().split()))
dp = [[-1 for _ in range(510)] for _ in range(510)]
for _ in range(5):
    a, b = map(int, input().split())
    answer = sol(a, b)
    if answer:
        print('A')
    else:
        print('B')


