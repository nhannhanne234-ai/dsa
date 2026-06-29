class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)
    
    def index(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1
    
a = ArrayList()
a.append(5)
a.append(3)
a.append(7)

print(a.index(7))