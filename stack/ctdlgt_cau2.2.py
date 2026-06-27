from collections import deque
q = deque()                                 # khởi tạo hàng đợi rỗng
q.append('data analytics')                  # thêm 'data science' vào cuối hàng đợi
q.append('data structures and algorithms')
q.append('big data')
q.append('learning data analytics')
print(q)
print(q.popleft())                          # lấy phần tử ở đầu hàng đợi
print(q.popleft())
print(q)