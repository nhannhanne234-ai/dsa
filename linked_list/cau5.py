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

    def deleteValue(self, x):
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current and current.data != x:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("null")

lst = SinglyLinkedList()
for x in [1, 2, 3, 2]:
    lst.pushBack(x)
lst.deleteValue(2)
lst.display()