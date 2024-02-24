import sys
input = sys.stdin.readline


def is_possible(info):
    total = sum(money * amount for money, amount in info)

    # 동전의 총합이 홀수인 경우, 두 사람이 공평하게 나눌 수 없음
    if total % 2 == 1:
        return 0

    half = total // 2
    dp = [0] * (half + 1)
    dp[0] = 1

    for money, amount in info:
        num = 1
        while amount > 0:
            k = min(num, amount)
            for i in range(half, money*k-1, -1):
                if dp[i - money*k] == 1:
                    dp[i] = 1
            amount -= k
            num *= 2

    return dp[-1]


for _ in range(3):
    N = int(input())
    coins = [tuple(map(int, input().split())) for _ in range(N)]
    print(is_possible(coins))
