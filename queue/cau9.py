def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited

g = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
    }
print(bfs(g, 2))