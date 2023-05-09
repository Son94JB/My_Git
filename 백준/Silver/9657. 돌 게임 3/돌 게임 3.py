def sol(num):

    if num < 0:
        return True
    if num == 0:
        return False

    if dp[num] != -1:
        return dp[num]

    cnt = 0
    for n in arr:
        if not sol(num-n):
            cnt += 1

    if cnt:
        dp[num] = True
    else:
        dp[num] = False

    return dp[num]


N = int(input())
arr = [1, 3, 4]
dp = [-1 for _ in range(1010)]

if sol(N):
    print('SK')
else:
    print('CY')

