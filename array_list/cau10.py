class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def merge(self, other):
        result = []
        i = 0
        j = 0
        while i < len(self.data) and j < len(other.data):
            if self.data[i] <= other.data[j]:
                result.append(self.data[i])
                i += 1
            else:
                result.append(other.data[j])
                j += 1
        while i < len(self.data):
            result.append(self.data[i])
            i += 1
        while j < len(other.data):
            result.append(other.data[j])
            j += 1
        return result


a1 = ArrayList()
a1.append(1)
a1.append(3)
a1.append(5)

a2 = ArrayList()
a2.append(2)
a2.append(4)

print(a1.merge(a2))