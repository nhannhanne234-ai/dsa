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

def dijkstra_basic(graph, start, n):
    infty_fake = 10**10
    dist = [infty_fake] * n
    visited = [False] * n
    dist[start] = 0
    pq = []
    heap_push(pq, (0, start))
    while len(pq) > 0:
        current_dist, u = heap_pop(pq)
        if visited[u]: continue
        visited[u] = True
        for next_peak, weight in graph[u]:
            if not visited[next_peak] and dist[u] + weight < dist[next_peak]:
                dist[next_peak] = dist[u] + weight
                heap_push(pq, (dist[next_peak], next_peak))
    return dist

def precompute_all_pairs_shortest_paths(graph, n):
    dist_matrix = []
    for i in range(n):
        dist_from_i = dijkstra_basic(graph, i, n)
        dist_matrix.append(dist_from_i)
    return dist_matrix

n_vertices = 6
g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

shortest_path_matrix = precompute_all_pairs_shortest_paths(g, n_vertices)
queries = [
    (0, 4),
    (0, 5),
    (2, 5),
    (1, 4)
]

for idx, (s, t) in enumerate(queries):
    ans = shortest_path_matrix[s][t]
    if ans >= 10**10:
        print(f"Truy vấn {idx + 1}: Từ {s} tới {t} -> Không có đường đi")
    else:
        print(f"Truy vấn {idx + 1}: Từ {s} tới {t} -> Khoảng cách ngắn nhất bằng: {ans}")