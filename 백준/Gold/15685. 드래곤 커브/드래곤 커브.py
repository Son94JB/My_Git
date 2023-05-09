import sys
input = sys.stdin.readline
N = int(input())
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
arr = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dirs = [d]
    for _ in range(g):
        temp = []
        for dd in range(len(dirs)-1, -1, -1):
            temp.append((dirs[dd]+1)%4)
        dirs += temp
    arr[x][y] = 1
    while dirs:
        idx = dirs.pop(0)
        x += dir[idx][0]
        y += dir[idx][1]
        arr[x][y] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]==1 and arr[i+1][j+1]==1:
            ans += 1
print(ans)