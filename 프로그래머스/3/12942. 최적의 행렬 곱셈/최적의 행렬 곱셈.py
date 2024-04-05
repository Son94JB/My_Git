def solution(matrix_sizes):
    # 행렬의 곱 순서에 따라 횟수가 바뀔 수 있는데 최소 횟수를 구하자.
    # 행렬의 크기가 리스트로 주어진다.
    n = len(matrix_sizes)
    # dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱했을 때의 최소 곱셈 횟수를 저장
    dp = [[0] * n for _ in range(n)]

    # chainLen은 현재 고려하고 있는 행렬 체인의 길이
    for chainLen in range(2, n + 1):
        for i in range(0, n - chainLen + 1):
            j = i + chainLen - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                # dp[i][k]와 dp[k+1][j]는 이미 계산된 최소값들
                # matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]는 현재 고려 중인 두 행렬 체인을 곱하는 비용
                cost = dp[i][k] + dp[k + 1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


