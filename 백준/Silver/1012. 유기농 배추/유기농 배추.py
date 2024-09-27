# 첫 줄에는 T, 둘째 줄에는 가로 세로(M, N) 길이와 배추의 개수가 주어진다.
# 그 밑으로는 배추의 위치가 X,Y로 주어진다. 위에서 부터 (0, 0)
# 배추흰지렁이는 인접한 배추들을 모두 지킬 수 있다.
# 모든 배추들을 지키려할 때 필요한 최소 배추흰지렁이의 개수를 구하라.
from collections import deque


def check_warm(data, n, m):
    # 전체 돌면서 배추가 붙어있는 부분에만 카운트를 올려준다.
    # 1이 나오면 카운트를 올리되, 방문에 넣고 다른 1과 연결된 부분도 순회하면서 방문 기록
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    def bfs(y, x):
        queue = deque([(y, x)])
        data[y][x] = 0

        while queue:
            cy, cx = queue.popleft()
            for direction in range(4):
                ny, nx = cy + dy[direction], cx + dx[direction]
                if 0 <= ny < n and 0 <= nx < m and data[ny][nx] == 1:
                    data[ny][nx] = 0
                    queue.append((ny, nx))

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:  # 배추가 있는 경우
                bfs(i, j)  # BFS 호출
                count += 1  # 새로운 덩어리 발견
    return count


T = int(input())
for i in range(T):
    M, N, cabbage = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for j in range(cabbage):
        x, y = map(int, input().split())
        farm[y][x] = 1

    result = check_warm(farm, N, M)  # 배추흰지렁이 개수 계산
    print(result)
