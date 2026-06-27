def josephus(n, k):
    queue = list(range(1, n + 1))
    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.pop(0))
        queue.pop(0)
    return queue[0]

print(josephus(5, 2))