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

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

lst = SinglyLinkedList()
lst.pushBack(1)
lst.pushBack(2)
lst.pushBack(3)
lst.display()
print(lst.length())