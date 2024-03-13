from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, L, R = map(int, input().split())

population = [list(map(int, input().split())) for _ in range(N)]


def bfs(sy, sx):
    visited[sy][sx] = True
    q = deque([(sy, sx)])
    temp = [(sy, sx)]  # 연합을 이루는 나라들의 좌표를 저장
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(population[y][x] - population[ny][nx]) <= R:
                    q.append((ny, nx))
                    temp.append((ny, nx))
                    visited[ny][nx] = True
    return temp


days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    is_moved = False  # 인구 이동이 일어났는지 체크
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                united = bfs(i, j)  # 연합을 찾는다
                if len(united) > 1:
                    is_moved = True
                    num = sum(population[y][x] for y, x in united) // len(united)
                    for y, x in united:
                        population[y][x] = num
    if not is_moved:
        break
    days += 1

print(days)
