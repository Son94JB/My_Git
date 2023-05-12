import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y, False)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 1

    while queue:
        x, y, gram = queue.popleft()

        if visited[x][y][0]-1 > T or visited[x][y][1]-1 > T:
            return 'Fail'

        if x == N-1 and y == M-1 and gram:
            return visited[x][y][1]-1
        elif x == N-1 and y == M-1 and not gram:
            return visited[x][y][0]-1

        for dr, dc in d:
            nx = x + dr
            ny = y + dc

            if gram:
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[x][y][1] + 1
                    queue.append((nx, ny, True))
            else:
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][0] and arr[nx][ny] != 1:
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    if arr[nx][ny] == 2:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        queue.append((nx, ny, True))
                    queue.append((nx, ny, False))

    return 'Fail'


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(bfs(0, 0))
