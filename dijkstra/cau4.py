def dijkstra(graph, peak):
    n = len(graph)                                          # lấy số lượng đỉnh
    infty_fake = 10**10                                     # giả lập vô hạn bằng số cực lớn
    dist = [infty_fake] * n                                 # tạo mảng với n phần tử vô hạn
    dist[peak] = 0                                          # đặt khoảng cách xuất phát từ đỉnh nguồn (peak) đến chính nó bằng 0
    visited = [False] * n                                   # khởi tạo mảng đánh dấu, False có nghĩa là đỉnh chưa tìm được đường đi ngắn nhất tuyệt đối

    for _ in range(n):                                      
        min_dist = infty_fake                               # đặt mốc tìm khoảng cách nhỏ nhất của lượt này là vô hạn
        u = -1                                              # u được chọn làm đỉnh tạm thời, tạm thời = -1 vì chưa tìm thấy

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:       # nếu đỉnh chưa duyệt xong và đỉnh đang xét nhỏ hơn móc nhỏ nhất là min_dist
                min_dist = dist[i]                          # cập nhật lại mốc nhỏ nhất mới
                u = i                                       # u sẽ là đỉnh i của lượt này
        
        if u == -1:                                         # nếu duyệt hết mảng mà u vẫn bằng -1 nghĩa là không có đường tới
            break                                           # thoát khỏi vòng lặp

        visited[u] = True                                   # khóa đỉnh u lại, đánh dấu đỉnh u đã tìm được đường đi ngắn nhất và chính xác nhất

# bước cập nhật (relaxation), duyệt qua từng đỉnh kề của u trong danh sách kề

        for next_peak, nums in graph[u]:                    # next_peak: tên đỉnh kề, nums: trọng số cạnh nối từ u sang next_peak
            if not visited[next_peak]:                      # chỉ xét nếu đỉnh kề (next_peak) này chưa bị khóa duyệt hoàn toàn
                if dist[u] + nums < dist[next_peak]:        # nếu (khoảng cách đến u + chi phí từ u sang next_peak) ngắn hơn đường cũ tới next_peak
                    dist[next_peak] = dist[u] + nums        # cập nhật (ghi đè) giá trị mới tối ưu hơn cho đỉnh kề đó
    
    return dist

g = {
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5),(4,8)],
    3:[(5,6),(4,3)],
    4:[(5,2)],
    5:[]
}

pk = 0
result = dijkstra(g, pk)
print(result)



dist = []

for x in result:
    if x != 10**10:
        dist.append(x)
    else:
        dist.append(-1)

# dist = [x if x != 10**10 else -1 for x in result]
print(dist[5])