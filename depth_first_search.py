# depth first search (dfs) on a graph
# goes as deep as possible down one path before backtracking

def dfs(graph, start):
    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def has_path(graph, start, target):
    # True if target can be reached from start
    return target in dfs(graph, start)


# example graph: keys are nodes, values are neighbours
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs(graph, 'A'))
print(has_path(graph, 'A', 'F'))
print(has_path(graph, 'A', 'Z'))
