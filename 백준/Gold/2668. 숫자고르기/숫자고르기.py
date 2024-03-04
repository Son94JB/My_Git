# 연결된 노드라고 생각?
# 결국 이어져있으면서 순환하는 노드들의 집합을 구해야 한다.


def dfs(cur, start):

    visited[cur] = True
    nxt = data[cur]

    if not visited[nxt]:
        dfs(nxt, start)
    elif visited[nxt] and nxt == start:
        result.append(nxt)


n = int(input())
data = [0]+[int(input()) for _ in range(n)]
result = []

for i in range(1, n+1):
    visited = [False]*(n+1)
    dfs(i, i)

print(len(result))
result.sort()
for i in result:
    print(i)
