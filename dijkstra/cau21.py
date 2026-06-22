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

def dijkstra_extended(graph, start, total_tickets):
    n = len(graph)
    infty_fake = 10**10
    dist = [[infty_fake] * (total_tickets + 1) for _ in range(n)]
    visited = [[False] * (total_tickets + 1) for _ in range(n)]
    dist[start][total_tickets] = 0
    pq = []
    heap_push(pq, (0, start, total_tickets))
    while len(pq) > 0:
        current_cost, u, rem_tickets = heap_pop(pq)
        if visited[u][rem_tickets]: 
            continue
        visited[u][rem_tickets] = True
        for next_peak, weight in graph[u]:
            if not visited[next_peak][rem_tickets]:
                if current_cost + weight < dist[next_peak][rem_tickets]:
                    dist[next_peak][rem_tickets] = current_cost + weight
                    heap_push(pq, (dist[next_peak][rem_tickets], next_peak, rem_tickets))
            if rem_tickets > 0:
                discount_weight = weight // 2
                new_tickets = rem_tickets - 1
                if not visited[next_peak][new_tickets]:
                    if current_cost + discount_weight < dist[next_peak][new_tickets]:
                        dist[next_peak][new_tickets] = current_cost + discount_weight
                        heap_push(pq, (dist[next_peak][new_tickets], next_peak, new_tickets))
    return dist

g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

start_node = 0
target_node = 5
K_tickets = 1

matrix_result = dijkstra_extended(g, start_node, K_tickets)
min_cost_to_target = min(matrix_result[target_node])

print(f"bảng trạng thái tại đích {target_node}: {matrix_result[target_node]}")
print(f"chi phí nhỏ nhất tới đích khi có {K_tickets} vé: {min_cost_to_target}")