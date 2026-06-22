def heap_push(heap, element):
    heap.append(element)
    i = len(heap) - 1
    parent = (i - 1) // 2
    while i > 0 and heap[i][0] < heap[parent][0]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent = (i - 1) // 2

def heap_pop(heap):
    if not heap: return None
    if len(heap) == 1: return heap.pop()
    root = heap[0]
    heap[0] = heap.pop()
    i, n = 0, len(heap)
    while 2 * i + 1 < n:
        left, right = 2 * i + 1, 2 * i + 2
        smallest = left
        if right < n and heap[right][0] < heap[left][0]: smallest = right
        if heap[i][0] <= heap[smallest][0]: break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return root

def dijkstra_bounded_edges(graph, start, target, max_stops):
    n = len(graph)
    infty_fake = 10**10
    max_edges = max_stops + 1
    dist = [[infty_fake] * (max_edges + 1) for _ in range(n)]
    visited = [[False] * (max_edges + 1) for _ in range(n)]
    dist[start][0] = 0
    pq = []
    heap_push(pq, (0, start, 0))
    while len(pq) > 0:
        current_cost, u, edges_used = heap_pop(pq)
        if visited[u][edges_used]: continue
        visited[u][edges_used] = True
        if edges_used >= max_edges:
            continue
        for next_peak, weight in graph[u]:
            next_edges = edges_used + 1
            if next_edges <= max_edges:
                if not visited[next_peak][next_edges]:
                    if current_cost + weight < dist[next_peak][next_edges]:
                        dist[next_peak][next_edges] = current_cost + weight
                        heap_push(pq, (dist[next_peak][next_edges], next_peak, next_edges))
    min_cost = infty_fake
    for e in range(max_edges + 1):
        if dist[target][e] < min_cost:
            min_cost = dist[target][e]
    return -1 if min_cost == infty_fake else min_cost

g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

start_node = 0
target_node = 4
k_stops = 1 

ans = dijkstra_bounded_edges(g, start_node, target_node, k_stops)

print(f"chi phí nhỏ nhất: {ans}")