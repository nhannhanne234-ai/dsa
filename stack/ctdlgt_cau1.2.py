from collections import deque                       # nhập thư viện deque để sử dụng làm cấu trúc dữ liệu stack
myStack = deque()
myStack.append('data science')                      # thêm "data science" vào mảng myStack
myStack.append('data structures and algorithms')
myStack.append('learning data analytics')
myStack.append('big data')
myStack
myStack.pop()                                       # bứng phần tử cuối của mảng myStack ra khỏi mảng
myStack.pop()
print(myStack)