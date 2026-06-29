class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    # def get(self, index):
    #     if len(self.data) > index >= 0:
    #         return self.data[index]
    #     return "ẹc ẹc lố rồi"

    # def set(self, index, value):
    #     if len(self.data) > index >= 0:
    #         self.data[index] = value
    #     return "ẹc ẹc lố kìa"

    # def size(self):
    #     return len(self.data)
    
    def popback(self):
        if len(self.data) == 0:
            return "rỗng mà đòi bóc"
        return self.data.pop()
    
    def lst(self):
        print(self.data)

    
a = ArrayList()
a.append(1)
a.append(2)
a.append(3)

a.lst()
x = a.popback()
print(f"{x} bị cút")
a.lst()