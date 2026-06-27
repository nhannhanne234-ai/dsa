class MonotonicDeque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push_back(self, index):
        self.items.append(index)

    def pop_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def pop_back(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def get_back(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def max_sliding_window(nums, k):
    dq = MonotonicDeque()
    res = []
    for i in range(len(nums)):
        if not dq.is_empty() and dq.get_front() < i - k + 1:
            dq.pop_front()
        while not dq.is_empty() and nums[dq.get_back()] < nums[i]:
            dq.pop_back()
        dq.push_back(i)
        if i >= k - 1:
            res.append(nums[dq.get_front()])
    return res

a = [1, 3, -1, -3, 5, 3]
print(max_sliding_window(a, 3))