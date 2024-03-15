import sys
from collections import deque


def solution(land):
    n = len(land)  # n x m 행렬
    m = len(land[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = [0 for _ in range(m)]  # 각 col에 대해 시추관을 뚫었을 때 얻을 수 있는 석유량
    answer = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j, visited, n, m, land, result)

    answer = max(result)  # 가장 많은 석유량

    return answer


def bfs(x, y, visited, n, m, land, result):
    queue = deque([(x, y)])
    visited[x][y] = True
    areaAmount = 0
    startY, endY = 501, -501  # 영역이 차지하는 col의 범위

    while queue:
        cx, cy = queue.popleft()
        areaAmount += 1
        startY, endY = min(startY, cy), max(endY, cy)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

    for col in range(startY, endY + 1):  # 해당 col범위에 대해 석유량 누적
        result[col] += areaAmount