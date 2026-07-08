class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def reverse(self, left, right):
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1

    def rotate_right(self, k):
        n = len(self.data)
        if n == 0:
            return
        k = k % n
        self.reverse(0, n - 1)
        self.reverse(0, k - 1)
        self.reverse(k, n - 1)

a = ArrayList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

a.rotate_right(2)

print(a.data)