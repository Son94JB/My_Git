def dfs(start):
    stack = list()
    stack.append(start)
    visited = set()
    while stack:
        o = stack.pop()
        if o not in visited:
            visited.add(o)
            answer.append(o+1)
            for i in range(N-1, -1, -1):
                if line[o][i] and i not in visited:
                    stack.append(i)


def bfs(start):
    queue = list()
    queue.append(start)
    visited = set()
    while queue:
        o = queue.pop(0)
        if o not in visited:
            visited.add(o)
            answer2.append(o+1)
            for i in range(N):
                if line[o][i] and i not in visited:
                    queue.append(i)


N, M, V = map(int, input().split())
line = [[0]*N for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    line[s-1][e-1] = 1
    line[e-1][s-1] = 1

answer = []
answer2 = []

dfs(V-1)
bfs(V-1)
print(*answer)
print(*answer2)
