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

def dijkstra_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    infty_fake = 10**10
    dist = [[infty_fake] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    pq = []
    heap_push(pq, (grid[0][0], 0, 0))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while len(pq) > 0:
        current_cost, r, c = heap_pop(pq)
        if visited[r][c]: continue
        visited[r][c] = True
        if r == rows - 1 and c == cols - 1:
            break
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc]:
                    weight = grid[nr][nc]
                    if current_cost + weight < dist[nr][nc]:
                        dist[nr][nc] = current_cost + weight
                        heap_push(pq, (dist[nr][nc], nr, nc))
    return dist[rows-1][cols-1]

matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

ans = dijkstra_grid(matrix)
print(f"tổng chi phí nhỏ nhất tới đích: {ans}")