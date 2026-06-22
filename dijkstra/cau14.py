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

def dijkstra_second_shortest(graph, start):
    n = len(graph)
    infty_fake = 10**10
    dist1 = [infty_fake] * n
    dist2 = [infty_fake] * n
    dist1[start] = 0
    pq = []
    heap_push(pq, (0, start))
    while len(pq) > 0:
        current_dist, u = heap_pop(pq)
        if current_dist > dist2[u]:
            continue
        for next_peak, weight in graph[u]:
            d = current_dist + weight
            if d < dist1[next_peak]:
                dist2[next_peak] = dist1[next_peak]
                dist1[next_peak] = d
                heap_push(pq, (dist1[next_peak], next_peak))
                heap_push(pq, (dist2[next_peak], next_peak))
            elif dist1[next_peak] < d < dist2[next_peak]:
                dist2[next_peak] = d
                heap_push(pq, (dist2[next_peak], next_peak))
    return dist1, dist2

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

d1, d2 = dijkstra_second_shortest(g, start_node)

print(f"ngắn nhất = {d1[target_node]}")
print(f"ngắn nhì = {d2[target_node]}")