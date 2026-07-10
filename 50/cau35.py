def merge(time):
    if not time:
        return []
    time.sort(key=lambda x: x[0])
    merge = [time[0]]
    for start, end in time[1:]:
        last = merge[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merge.append([start, end])
    return merge

time = [[1,3], [2,6], [8,10]]
print(merge(time))