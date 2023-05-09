def dfs(n):
    stack = []
    visited = set()

    stack.append(n)
    while stack:
        t = stack.pop()
        visited.add(t)

        for i in range(N):
            if not connection[t][i] or i in visited:
                continue
            elif connection[t][i]:
                stack.append(i)

    return len(visited)


N = int(input())
M = int(input())

connection = [[0]*N for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    connection[s-1][e-1] = 1
    connection[e-1][s-1] = 1

ans = dfs(0) - 1
print(ans)
