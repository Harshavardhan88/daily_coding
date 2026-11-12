# dijkstra's algorithm - shortest path from one node to all others

import heapq


def dijkstra(graph, start):
    # distance to each node, infinity to start with except the start node
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = set()
    # heap of (distance, node) so we always pick the closest unvisited node
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        for neighbour, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(heap, (new_dist, neighbour))

    return dist


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

print(dijkstra(graph, 'A'))
print(dijkstra(graph, 'B'))
