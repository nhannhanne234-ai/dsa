class ArrayList:
    def __init__(self):
        self.data = []

    def remove_dup(self):
        result = []
        for x in self.data:
            found = False
            for y in result:
                if x == y:
                    found = True
                    break
            if not found:
                result.append(x)
        self.data = result

a = ArrayList()
a.data = [3, 1, 3, 2, 1, 3, 1, 3, 2, 1, 3, 1, 3, 2, 1, 3, 1, 3, 2, 1, 3, 1, 3, 2, 1, 3, 1, 3, 2, 1, 3, 1, 3, 2, 1]
a.remove_dup()
print(a.data)