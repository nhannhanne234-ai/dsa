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

def solve_dijkstra(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    infty = 10**10
    dist = [[infty] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]]
    pq = []
    heap_push(pq, (dist[start[0]][start[1]], start[0], start[1]))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    nodes_explored = 0
    while pq:
        current_g, r, c = heap_pop(pq)
        if visited[r][c]: continue
        visited[r][c] = True
        nodes_explored += 1
        if (r, c) == target:
            return current_g, nodes_explored
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if current_g + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = current_g + grid[nr][nc]
                    heap_push(pq, (dist[nr][nc], nr, nc))
    return -1, nodes_explored

def solve_astar(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    infty = 10**10
    g_score = [[infty] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    def heuristic(r, c):
        return abs(r - target[0]) + abs(c - target[1])
    g_score[start[0]][start[1]] = grid[start[0]][start[1]]
    initial_f = g_score[start[0]][start[1]] + heuristic(start[0], start[1])
    pq = []
    heap_push(pq, (initial_f, g_score[start[0]][start[1]], start[0], start[1]))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    nodes_explored = 0
    while pq:
        current_f, current_g, r, c = heap_pop(pq)
        if visited[r][c]: continue
        visited[r][c] = True
        nodes_explored += 1
        if (r, c) == target:
            return current_g, nodes_explored
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if current_g + grid[nr][nc] < g_score[nr][nc]:
                    g_score[nr][nc] = current_g + grid[nr][nc]
                    next_f = g_score[nr][nc] + heuristic(nr, nc)
                    heap_push(pq, (next_f, g_score[nr][nc], nr, nc))
    return -1, nodes_explored

map_grid = [[1] * 15 for _ in range(15)]
start_point = (0, 0)
target_point = (14, 14)

dijkstra_cost, dijkstra_nodes = solve_dijkstra(map_grid, start_point, target_point)
astar_cost, astar_nodes = solve_astar(map_grid, start_point, target_point)

print(f"thuật toán Dijkstra, tổng chi phí: {dijkstra_cost}, số đỉnh phải duyệt: {dijkstra_nodes}")
print(f"thuật toán A*, tổng chi phí: {astar_cost}, số đỉnh phải duyệt: {astar_nodes}")