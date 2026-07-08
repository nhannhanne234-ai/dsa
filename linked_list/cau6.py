class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def pushBack(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("null")

# lặp
    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# đệ quy
    def reverse_recursive(self):
        self.head = self._reverse(self.head)
    def _reverse(self, node):
        if node is None or node.next is None:
            return node
        new_head = self._reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head

lst = SinglyLinkedList()
for x in [1, 2, 3]:
    lst.pushBack(x)
lst.display()
lst.reverse_iterative()
lst.display()