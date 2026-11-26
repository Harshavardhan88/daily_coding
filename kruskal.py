# Kruskal's algorithm - minimum spanning tree
# sort all edges by weight, then keep adding the cheapest
# edge that doesn't form a cycle. union-find tracks which
# vertices are already connected.

def kruskal(num_vertices, edges):
    # edges are (weight, u, v)
    parent = list(range(num_vertices))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    mst = []
    total = 0
    for weight, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, weight))
            total += weight
        if len(mst) == num_vertices - 1:
            break
    return mst, total


# example: 4 vertices, edges as (weight, u, v)
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3),
]

mst, total = kruskal(4, edges)
print("mst edges:", mst)
print("total weight:", total)

# a bigger example
edges2 = [
    (1, 0, 1), (4, 0, 2), (3, 1, 2),
    (2, 1, 3), (5, 2, 3), (6, 3, 4),
    (7, 2, 4),
]
mst2, total2 = kruskal(5, edges2)
print("mst edges:", mst2)
print("total weight:", total2)
