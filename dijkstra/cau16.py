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

def dijkstra_vertex_weights(graph, vertex_costs, start):
    n = len(graph)
    infty_fake = 10**10
    dist = [infty_fake] * n
    visited = [False] * n
    dist[start] = vertex_costs[start]
    pq = []
    heap_push(pq, (dist[start], start))
    while len(pq) > 0:
        current_dist, u = heap_pop(pq)
        if visited[u]: continue
        visited[u] = True
        for next_peak, edge_weight in graph[u]:
            if not visited[next_peak]:
                total_weight = edge_weight + vertex_costs[next_peak]
                if dist[u] + total_weight < dist[next_peak]:
                    dist[next_peak] = dist[u] + total_weight
                    heap_push(pq, (dist[next_peak], next_peak))
    return dist

g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

costs = [10, 2, 5, 1, 4, 3]
result_dist = dijkstra_vertex_weights(g, costs, 0)

print("khoảng cách ngắn nhất, tính cả chi phí đỉnh):", result_dist)