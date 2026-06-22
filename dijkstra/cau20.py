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

def dijkstra_k_shortest(graph, start, target, k):
    n = len(graph)
    count = [0] * n
    result_paths = []
    pq = []
    heap_push(pq, (0, start))
    while len(pq) > 0:
        current_dist, u = heap_pop(pq)
        if count[u] >= k:
            continue
        count[u] += 1
        if u == target:
            result_paths.append(current_dist)
            if len(result_paths) == k:
                break
        for next_peak, weight in graph[u]:
            if count[next_peak] < k:
                new_dist = current_dist + weight
                heap_push(pq, (new_dist, next_peak))
    return result_paths

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
K = 3
k_shortest_lengths = dijkstra_k_shortest(g, start_node, target_node, K)

print(f"-> Kết quả đầu ra: {k_shortest_lengths}")