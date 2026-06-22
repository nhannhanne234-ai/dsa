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

def multi_source_dijkstra(graph, sources):
    n = len(graph)
    dist = [10**10] * n
    visited = [False] * n
    pq = []
    for s in sources:
        dist[s] = 0
        heap_push(pq, (0, s))
    while len(pq) > 0:
        current_dist, u = heap_pop(pq)
        if visited[u]: continue
        visited[u] = True
        for next_peak, weight in graph[u]:
            if not visited[next_peak] and dist[u] + weight < dist[next_peak]:
                dist[next_peak] = dist[u] + weight
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

source = [0, 3]

result_dist = multi_source_dijkstra(g, source)

print(f"tập nguồn = {set(source)}")
print(f"mảng khoảng cách tới nguồn gần nhất là: {result_dist}")