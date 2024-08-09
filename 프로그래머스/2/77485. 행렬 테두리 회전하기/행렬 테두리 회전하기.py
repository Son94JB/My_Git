def solution(rows, columns, queries):
    # 초기 그래프 설정
    graph = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    min_values = []
    
    for query in queries:
        sy, sx, ey, ex = [q - 1 for q in query]  # 1-based index를 0-based로 변환

        # 회전할 테두리의 값들을 저장
        temp = []
        for i in range(sx, ex):  # 상단 (왼 -> 오)
            temp.append(graph[sy][i])
        for i in range(sy, ey):  # 오른쪽 (위 -> 아래)
            temp.append(graph[i][ex])
        for i in range(ex, sx, -1):  # 하단 (오 -> 왼)
            temp.append(graph[ey][i])
        for i in range(ey, sy, -1):  # 왼쪽 (아래 -> 위)
            temp.append(graph[i][sx])

        # 최솟값을 저장
        min_values.append(min(temp))

        # 회전된 값들을 테두리에 다시 삽입
        temp = [temp[-1]] + temp[:-1]  # 시계 방향으로 회전

        idx = 0
        for i in range(sx, ex):  # 상단 (왼 -> 오)
            graph[sy][i] = temp[idx]
            idx += 1
        for i in range(sy, ey):  # 오른쪽 (위 -> 아래)
            graph[i][ex] = temp[idx]
            idx += 1
        for i in range(ex, sx, -1):  # 하단 (오 -> 왼)
            graph[ey][i] = temp[idx]
            idx += 1
        for i in range(ey, sy, -1):  # 왼쪽 (아래 -> 위)
            graph[i][sx] = temp[idx]
            idx += 1

    return min_values