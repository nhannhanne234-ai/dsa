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

def dijkstra_count_paths(graph, start):
    n = len(graph)
    infty_fake = 10**10
    dist = [infty_fake] * n
    visited = [False] * n
    ways = [0] * n
    dist[start] = 0
    ways[start] = 1
    pq = []
    heap_push(pq, (0, start))
    while len(pq) > 0:
        current_dist, u = heap_pop(pq)
        if visited[u]: continue
        visited[u] = True
        for next_peak, weight in graph[u]:
            if not visited[next_peak]:
                if dist[u] + weight < dist[next_peak]:
                    dist[next_peak] = dist[u] + weight
                    ways[next_peak] = ways[u]
                    heap_push(pq, (dist[next_peak], next_peak))
                elif dist[u] + weight == dist[next_peak]:
                    ways[next_peak] += ways[u]
    return dist, ways

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

distances, path_counts = dijkstra_count_paths(g, start_node)

print(f"độ dài đường đi ngắn nhất: {distances[target_node]}")
print(f"số lượng đường đi ngắn nhất khác nhau: {path_counts[target_node]}")