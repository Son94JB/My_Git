from collections import deque

def bfs(si, sj):
    global cnt, ans

    dq = deque()
    dq.append((si, sj))

    while dq:
        ci, cj = dq.popleft()

        if ci == N-1 and cj == M-1:
            return visited[ci][cj]

        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maze[ni][nj] == '1':
                dq.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1

ans = bfs(0, 0)
print(ans)
