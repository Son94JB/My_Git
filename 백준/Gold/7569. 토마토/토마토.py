import sys
input = sys.stdin.readline
from collections import deque
def sol():
    cnt = 0
    while q:
        for _ in range(len(q)):
            h, i, j = q.popleft()

            for dh, di, dj in d:
                if h+dh < 0 or h+dh >= H or i+di >= N or i+di < 0 or j+dj < 0 or j+dj >= M:
                    continue
                if box[h+dh][i+di][j+dj] == -1 or box[h+dh][i+di][j+dj] == 1:
                    continue
                if (h+dh, i+di, j+dj) in visited:
                    continue
                box[h+dh][i+di][j+dj] = 1
                q.append([h+dh, i+di, j+dj])
                visited.add((h+dh, i+di, j+dj))
        if q:
            cnt += 1

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] == 0:
                    return -1
    return cnt
M, N, H = map(int, input().split())
box = []
q = deque()
visited = set()
zcnt = 0
for h in range(H):
    temp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 1:
                q.append([h, i, j])
                visited.add((h, i, j))
            elif temp[i][j] == 0:
                zcnt += 1
    box.append(temp)

d = [(0, 1, 0), (0, 0, -1), (0, -1, 0), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]


if zcnt == 0:
    print(0)
else:
    print(sol())
