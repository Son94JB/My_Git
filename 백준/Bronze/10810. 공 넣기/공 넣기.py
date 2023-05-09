N, M = map(int, input().split())
box = [0]*N
for _ in range(M):
    s, e, num = map(int, input().split())
    for i in range(s-1, e):
        box[i] = num

print(*box)
