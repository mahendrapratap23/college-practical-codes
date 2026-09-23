# Graph Traversal using DFS and BFS

import time

# Random graph
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

# DFS
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, visited)

# BFS
def bfs(start):
    visited = {start}
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# DFS
start = time.time()
print("DFS:", end=" ")
dfs(0, set())
print()
print("DFS Time:", time.time() - start)

# BFS
start = time.time()
print("BFS:", end=" ")
bfs(0)
print()
print("BFS Time:", time.time() - start)

print("Time Complexity: O(V + E)")

# Time Complexity: O(V + E)

# Output:
# DFS: 0 1 3 2 4
# DFS Time: 3.9577484130859375e-05
# BFS: 0 1 2 3 4
# BFS Time: 2.193450927734375e-05
# Time Complexity: O(V + E)