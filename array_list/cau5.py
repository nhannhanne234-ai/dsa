class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def count_even(self):
        count = 0
        for x in self.data:
            if x % 2 == 0:
                count += 1
        return count
    
    def count_odd(self):
        count = 0
        for x in self.data:
            if x % 2 != 0:
                count += 1
        return count
    
a = ArrayList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

print(a.count_even())
print(a.count_odd())