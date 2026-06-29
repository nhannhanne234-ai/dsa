class ArrayList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def get(self, index):
        if len(self.data) > index >= 0:
            return self.data[index]
        return "ẹc ẹc lố rồi"

    def set(self, index, value):
        if len(self.data) > index >= 0:
            self.data[index] = value
        return "ẹc ẹc lố kìa"

    def size(self):
        return len(self.data)
    
a = ArrayList()
a.add(1)
a.add(2)
a.add(3)

print(a.get(1))