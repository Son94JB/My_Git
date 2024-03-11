import heapq

def dijkstra(start, N, graph):
    heap = [(0, start)]
    cost = [float('inf')] * N
    cost[start] = 0

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_cost > cost[current_node]:
            continue

        for next_node, next_cost in graph[current_node]:
            new_cost = current_cost + next_cost

            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return cost


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A - 1].append((B - 1, C))
    graph[B - 1].append((A - 1, C))

start_node = 0
end_node = N - 1

min_costs = dijkstra(start_node, N, graph)
min_cost = min_costs[end_node]

print(min_cost)
