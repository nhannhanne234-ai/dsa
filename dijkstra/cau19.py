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

def dijkstra_max_probability(graph, start):
    n = len(graph)
    prob = [0.0] * n
    visited = [False] * n
    prob[start] = 1.0
    pq = []
    heap_push(pq, (-1.0, start))
    while len(pq) > 0:
        neg_p, u = heap_pop(pq)
        current_p = -neg_p
        if visited[u]: continue
        visited[u] = True
        for next_peak, weight in graph[u]:
            if not visited[next_peak]:
                new_prob = current_p * weight
                if new_prob > prob[next_peak]:
                    prob[next_peak] = new_prob
                    heap_push(pq, (-new_prob, next_peak))
    return prob

g = {
    0: [(1, 0.4), (2, 0.8)],
    1: [(3, 0.5)],
    2: [(1, 0.6), (3, 0.2), (4, 0.3)],
    3: [(5, 0.7), (4, 0.9)],
    4: [(5, 0.9)],
    5: []
}

start_node = 0
target_node = 5
result_probs = dijkstra_max_probability(g, start_node)

print(f"tích xác suất tối ưu: {result_probs[target_node]:.4f}")