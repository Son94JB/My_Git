import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(num, n, caves):
    sx, sy = 0, 0
    q = []
    heapq.heappush(q, (caves[sy][sx], sy, sx))
    distance = [[float('inf')] * n for _ in range(n)]
    distance[sy][sx] = caves[sy][sx]

    while q:
        dist, cy, cx = heapq.heappop(q)
        if cx == n-1 and cy == n-1:
            return print(f"Problem {num}: {dist}")
        if distance[cy][cx] < dist:
            continue
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            cost = dist + caves[ny][nx]
            if cost < distance[ny][nx]:
                distance[ny][nx] = cost
                heapq.heappush(q, (cost, ny, nx))


num = 1

while True:
    N = int(input())
    if N != 0:
        cave = [list(map(int, input().split())) for _ in range(N)]
        solution(num, N, cave)
        num += 1
    else:
        break
