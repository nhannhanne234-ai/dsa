class DynamicMatrix:
    def __init__(self):
        self.data = []

    def add_row(self, values=None):
        if values is None:
            values = []
        self.data.append(values)

    def add_column(self, default=None):
        for row in self.data:
            row.append(default)

    def set(self, i, j, value):
        self.data[i][j] = value

    def get(self, i, j):
        return self.data[i][j]

m = DynamicMatrix()

m.add_row([1, 2, 3])
m.add_row([4, 5, 6])

m.add_column(0)