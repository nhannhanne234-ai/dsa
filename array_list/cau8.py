class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def remove_if_even(self):
        write = 0
        for i in range(len(self.data)):
            if self.data[i] % 2 != 0:
                self.data[write] = self.data[i]
                write += 1
        self.data = self.data[:write]

a = ArrayList()

a.append(1)
a.append(2)
a.append(3)
a.append(4)

print(a.data)

a.remove_if_even()

print(a.data)