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

def dijkstra_heap(graph, start):
    n = len(graph)
    infty_fake = 10**10
    dist = [infty_fake] * n
    parent = [-1] * n
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
                parent[next_peak] = u
                heap_push(pq, (dist[next_peak], next_peak))
    return dist, parent

def trace_path(parent, target):
    path = []
    current = target
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

s = 0
t = 5
k = 2

# lần 1: chạy dijkstra từ nguồn s để tìm đường tới k
dist_from_s, parent_from_s = dijkstra_heap(g, s)

# lần 2: chạy dijkstra từ nguồn k để tìm đường tới t
dist_from_k, parent_from_k = dijkstra_heap(g, k)

# tính toán tổng độ dài ngắn nhất bắt buộc qua k
total_dist = dist_from_s[k] + dist_from_k[t]

# truy vết chi tiết đường đi hai chặng
path_s_to_k = trace_path(parent_from_s, k)
path_k_to_t = trace_path(parent_from_k, t)

# gộp hai chặng lại thành một đường đi liền mạch, bỏ bớt 1 phần tử trùng k ở giữa
full_path = path_s_to_k + path_k_to_t[1:]
chuoi_duong_di = " --> ".join(str(vertex) for vertex in full_path)

print(f"đường đi: {chuoi_duong_di}")
print(f"tổng độ dài: {total_dist}")