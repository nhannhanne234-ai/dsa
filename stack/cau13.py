class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def dfs_stack(graph, start):
    stack = Stack()
    visited = set()
    result = []
    stack.push(start)
    while not stack.is_empty():
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.push(neighbor)
    return result

g = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
    }
print(dfs_stack(g, 1))