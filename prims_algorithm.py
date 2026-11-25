# prim's algorithm - minimum spanning tree of a weighted graph

import heapq


def prims_mst(graph, start):
    # graph is a dict: node -> list of (neighbour, weight)
    # returns list of (from_node, to_node, weight) edges in the mst
    visited = {start}
    edges = []
    total = 0

    # start with all edges leaving the first node
    heap = []
    for neighbour, weight in graph[start]:
        heapq.heappush(heap, (weight, start, neighbour))

    while heap and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(heap)
        if to in visited:
            continue
        visited.add(to)
        edges.append((frm, to, weight))
        total += weight

        for neighbour, w in graph[to]:
            if neighbour not in visited:
                heapq.heappush(heap, (w, to, neighbour))

    return edges, total


# example graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)],
}

edges, total = prims_mst(graph, 'A')
print("mst edges:", edges)
print("total weight:", total)

# another run, starting from a different node
edges2, total2 = prims_mst(graph, 'D')
print("mst edges from D:", edges2)
print("total weight from D:", total2)
