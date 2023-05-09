import sys
input = sys.stdin.readline

N, H = map(int, input().split())
cave = [0]*(H+1)
prefix = [0]*(H+1)
stone = []
for a in range(N):
    stone.append(int(input()))
idx = 1
for i in stone:
    idx = (idx+1) % 2
    if not idx:
        cave[0] += 1
        cave[i] -= 1
    else:
        cave[H - i] += 1
prefix[0] = cave[0]
for i in range(len(cave)-1):
    prefix[i+1] = prefix[i]+cave[i+1]
prefix.pop()
min_len = min(prefix)
print(min_len, prefix.count(min_len))
