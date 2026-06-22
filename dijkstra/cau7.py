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
target = 4

result_dist, parent = dijkstra_with_path(g, start)

path = []
current = target

while current != -1:
    path.append(current)
    current = parent[current]

path.reverse()

chuoi_duong_di = " -> ".join(str(vertex) for vertex in path)
print(f"Ví dụ: {chuoi_duong_di} (độ dài {result_dist[target]})")