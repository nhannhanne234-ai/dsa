import time

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
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = left
        if right < n and heap[right][0] < heap[left][0]: smallest = right
        if heap[i][0] <= heap[smallest][0]: break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return root

def dijkstra_matrix(graph, start):
    n = len(graph)
    dist = [10**10] * n
    visited = [False] * n
    dist[start] = 0

    for _ in range(n):
        min_dist, u = 10**10, -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist, u = dist[i], i
        if u == -1: break
        visited[u] = True
        for next_peak, weight in graph[u]:
            if not visited[next_peak] and dist[u] + weight < dist[next_peak]:
                dist[next_peak] = dist[u] + weight
    return dist

def dijkstra_heap(graph, start):
    n = len(graph)
    dist = [10**10] * n
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

V = 3000
sparse_graph = {i: [] for i in range(V)}
for i in range(V - 1):
    sparse_graph[i].append((i + 1, 2))
    sparse_graph[i].append(((i + 2) % V, 5))

# đo thời gian bản Mảng O(V^2)
t0 = time.time()
dijkstra_matrix(sparse_graph, 0)
t_matrix = time.time() - t0

# đo thời gian bản Heap O((V+E)logV)
t0 = time.time()
dijkstra_heap(sparse_graph, 0)
t_heap = time.time() - t0

print(f"thử nghiệm V={V}:")
print(f"-> thời gian bản Mảng O(V^2): {t_matrix:.4f} giây")
print(f"-> thời gian bản Heap: {t_heap:.4f} giây")