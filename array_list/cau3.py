class ArrayList:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        if len(self.data) > index >= 0:
            self.data.insert(index, value)
        return "chọn sai chỗ nha"
    
    def remove(self, index):
        if len(self.data) > index >= 0:
            return self.data.pop(index)
        return "chắc chỗ đó có số không:v"
    
a = ArrayList()
a.data = [1, 3, 4]

print(a.data)

a.insert(1, 2)
print(a.data)

a.remove(3)
print(a.data)