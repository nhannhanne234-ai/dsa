def question_three(n, edges, start):
    distance = [10**9] * n
    distance[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] != 10**9 and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    return distance

n = 3
edges = [
    (0, 1, 2),
    (0, 2, 5),
    (2, 1, -4)
]
distance = question_three(n, edges, 0)
for i in range(n):
    print("A ->", chr(i + 65), "=", distance[i])