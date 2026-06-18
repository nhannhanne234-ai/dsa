def dijkstra_early_stopping(graph, peak, target):
    n = len(graph)
    infty_fake = 10**10
    dist = [infty_fake] * n
    dist[peak] = 0
    visited = [False] * n

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

        if u == target:
            break

        for next_peak, nums in graph[u]:                    
            if not visited[next_peak]:                      
                if dist[u] + nums < dist[next_peak]:        
                    dist[next_peak] = dist[u] + nums        
    
    return dist


g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

s = 0
t = 4

result = dijkstra_early_stopping(g, peak=s, target=t)

dist = []
for x in result:
    if x != 10**10:
        dist.append(x)
    else:
        dist.append(-1)

print(dist[t])