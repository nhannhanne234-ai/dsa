def dijkstra_with_path(graph, peak):
    n = len(graph)
    infty_fake = 10**10
    dist = [infty_fake] * n
    dist[peak] = 0
    visited = [False] * n
    parent = [-1] * n

    for _ in range(n):
        min_dist = infty_fake
        u = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        if u == -1:
            break

        visited[u] = True

        for next_peak, nums in graph[u]:
            if not visited[next_peak]:
                if dist[u] + nums < dist[next_peak]:
                    dist[next_peak] = dist[u] + nums
                    parent[next_peak] = u
    
    return dist, parent

g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

start = 0
D = 3

result_dist, _ = dijkstra_with_path(g, start)

danh_sach_dinh = []
for i in range(len(result_dist)):
    if result_dist[i] <= D:
        danh_sach_dinh.append(i)

so_luong_dinh = len(danh_sach_dinh)

print(f"D = {D} -> {so_luong_dinh} đỉnh {tuple(danh_sach_dinh)}")