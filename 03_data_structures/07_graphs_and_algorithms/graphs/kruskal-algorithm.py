# Disjoint Set (Union-Find) Data Structure
class DisjointSet:
    def __init__(self, vertices):
        # Each vertex is its own parent initially
        self.parent = {v: v for v in vertices}
        # Rank is used to keep trees balanced
        self.rank = {v: 0 for v in vertices}

    def find(self, u):
        # Path compression optimization
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by rank optimization
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# Kruskal’s Algorithm
def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(vertices)
    mst = []  # Minimum Spanning Tree edges

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):  # Avoid cycles
            ds.union(u, v)
            mst.append((u, v, w))
    return mst


# Define vertices
vertices = ['A', 'B', 'C', 'E', 'F', 'H']

# Define edges (u, v, weight)
edges = [
    ('B', 'F', 1),
    ('A', 'F', 2),
    ('B', 'A', 3),
    ('B', 'E', 4),
    ('F', 'A', 4),
    ('A', 'C', 4),
    ('C', 'H', 5),
    ('A', 'H', 7)
]

# Run Kruskal’s algorithm
mst = kruskal(vertices, edges)

print("Edges in Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")