from collections import deque

direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def solution(maps):
    result = bfs(maps)
    answer = result[len(maps)-1][len(maps[0])-1]
    return answer if answer != 0 else -1


def bfs(graph):
    start = [0, 0]
    q = deque([start])
    visited = set()

    y_len = len(graph)
    x_len = len(graph[0])

    distance = [[0 for _ in range(x_len)] for _ in range(y_len)]
    distance[0][0] = 1  # 시작점의 거리

    while q:
        cur_node = q.popleft()
        x, y = cur_node

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for d in direction:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < y_len and 0 <= ny < x_len and graph[nx][ny] == 1:
                if (nx, ny) not in visited:
                    q.append([nx, ny])
                    distance[nx][ny] = distance[x][y] + 1

    return distance