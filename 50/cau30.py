def round_robin(processes, quantum):
    queue = [[p[0], p[1]] for p in processes]
    time = 0
    res = {}
    while queue:
        pid, remaining_time = queue.pop(0)
        if remaining_time <= quantum:
            time += remaining_time
            res[pid] = time
        else:
            time += quantum
            queue.append([pid, remaining_time - quantum])
    return dict(sorted(res.items()))

processes = [("P1", 5), ("P2", 2), ("P3", 3)]
print(round_robin(processes, 2))