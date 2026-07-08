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

    def insertAfter(self, k, value):
        current = self.head
        index = 0
        while current and index < k:
            current = current.next
            index += 1
        if current is None:
            print("efeeee, vị trí không vừa ý")
            return
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("null")

lst = SinglyLinkedList()
lst.pushBack(1)
lst.pushBack(3)
lst.insertAfter(0, 2)
lst.display()