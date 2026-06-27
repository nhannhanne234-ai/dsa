from queue import Queue
q = Queue(maxsize = 5)
print(q.qsize())
q.put('data analytics')                    # thêm phần tử vào cuối hàng đợi
q.put('data structures and algorithms')
q.put('big data')
q.put('learning data analytics')
print(q.qsize())
print(q.get())                            # lấy phần tử ở đầu hàng đợi ra (FIFO)
print(q.get())