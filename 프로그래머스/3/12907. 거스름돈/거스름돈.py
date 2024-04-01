def solution(n, money):
    # dp[i]는 금액 i를 만들 수 있는 경우의 수를 의미
    dp = [0] * (n + 1)
    dp[0] = 1  # 금액이 0인 경우는 아무것도 선택하지 않는 1가지

    # 각 동전을 하나씩 순회하며
    for coin in money:
        # 해당 동전을 사용하여 만들 수 있는 금액들에 대해 경우의 수 계산
        for i in range(coin, n + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    
    answer = dp[n] % 1000000007
    return answer