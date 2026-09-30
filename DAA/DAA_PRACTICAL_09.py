# Minimum Spanning Tree (MST) using Prim's Algorithm

import time

# Weighted graph represented as an adjacency list
# node: [(neighbour, weight), ...]
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 1), (3, 4)],
    2: [(0, 3), (1, 1), (4, 5)],
    3: [(1, 4), (4, 6)],
    4: [(2, 5), (3, 6)]
}

# Prim's Algorithm
def prim(start):
    visited = {start}
    mst_edges = []
    total_cost = 0

    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None

        for u in visited:
            for neighbour, weight in graph[u]:
                if neighbour not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (u, neighbour, weight)

        if min_edge is None:
            break

        u, v, weight = min_edge
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_cost += weight

    return mst_edges, total_cost


# Prim's Algorithm
start = time.time()
mst_edges, total_cost = prim(0)
prim_time = time.time() - start

print("Edges in MST:")
for u, v, weight in mst_edges:
    print(f"{u} - {v} with weight {weight}")

print("Total Cost of MST:", total_cost)
print("Prim's Time:", prim_time)
print("Time Complexity: O(V^2)")

# Time Complexity: O(V^2)

# Output:
# Edges in MST:
# 0 - 1 with weight 2
# 1 - 2 with weight 1
# 1 - 3 with weight 4
# 2 - 4 with weight 5
# Total Cost of MST: 12
# Prim's Time: 1.0013580322265625e-05
# Time Complexity: O(V^2)

