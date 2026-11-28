# Bellman-Ford algorithm - shortest path from one start node,
# works even when some edges have negative weights.

def bellman_ford(edges, nodes, start):
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}

    # relax every edge again and again
    for _ in range(len(nodes) - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                changed = True
        if not changed:
            break

    # one more pass - if anything still relaxes, there is a negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None, None

    return dist, prev


def shortest_path(prev, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return path[::-1]


edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 3),
    ('B', 'D', 2),
    ('B', 'E', 3),
    ('C', 'B', 1),
    ('C', 'D', 4),
    ('C', 'E', 5),
    ('E', 'D', -5),
]
nodes = ['A', 'B', 'C', 'D', 'E']

dist, prev = bellman_ford(edges, nodes, 'A')
print("shortest distances from A:", dist)
print("shortest path to D:", shortest_path(prev, 'D'))

# graph with a negative cycle
bad_edges = [('X', 'Y', 1), ('Y', 'Z', -2), ('Z', 'X', -1)]
dist2, prev2 = bellman_ford(bad_edges, ['X', 'Y', 'Z'], 'X')
print("negative cycle found:", dist2 is None)
