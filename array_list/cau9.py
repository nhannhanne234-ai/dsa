class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def reverse(self):
        left = 0
        right = len(self.data) - 1
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1


a = ArrayList()

a.append(1)
a.append(2)
a.append(3)
a.append(4)

print(a.data)

a.reverse()

print(a.data)