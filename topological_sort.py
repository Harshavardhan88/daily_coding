# topological sort - order tasks so every dependency comes first
# kahn's algorithm: keep taking nodes with no incoming edges

from collections import deque


def topological_sort(graph):
    # graph is a dict: node -> list of nodes it points to
    in_degree = {}
    for node in graph:
        if node not in in_degree:
            in_degree[node] = 0
        for neighbour in graph[node]:
            in_degree[neighbour] = in_degree.get(neighbour, 0) + 1

    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, []):
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    # if some nodes are left out, the graph has a cycle
    if len(order) != len(in_degree):
        return None
    return order


def has_cycle(graph):
    return topological_sort(graph) is None


# course schedule: to take a course you must finish its prerequisites first
courses = {
    "maths": ["physics"],
    "physics": ["electronics"],
    "electronics": [],
    "programming": ["data_structures"],
    "data_structures": ["algorithms"],
    "algorithms": []
}

print(topological_sort(courses))

# build order: compile utils before the modules that use them
build = {
    "utils": ["parser", "logger"],
    "parser": ["app"],
    "logger": ["app"],
    "app": []
}

print(topological_sort(build))

# a graph with a cycle has no valid order
cyclic = {
    "a": ["b"],
    "b": ["c"],
    "c": ["a"]
}

print(topological_sort(cyclic))
print("has cycle:", has_cycle(cyclic))
print("has cycle:", has_cycle(courses))
