# breadth first search
# visits nodes level by level, so it finds the shortest path in an unweighted graph

def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


def bfs_shortest_path(graph, start, goal):
    # returns the shortest path from start to goal, or None if there is none
    queue = [[start]]
    seen = [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.append(neighbour)
                queue.append(path + [neighbour])

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

print(bfs(graph, 'A'))
print(bfs_shortest_path(graph, 'A', 'F'))
print(bfs_shortest_path(graph, 'A', 'D'))
print(bfs_shortest_path(graph, 'D', 'C'))
