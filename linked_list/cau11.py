class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def pushBack(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def popFront(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def popBack(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def displayForward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("null")

    def displayBackward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("null")

dll = DoublyLinkedList()
dll.pushFront(2)
dll.pushFront(1)
dll.pushBack(3)
dll.pushBack(4)
dll.displayForward()
dll.displayBackward()
dll.popFront()
dll.popBack()
dll.displayForward()
dll.displayBackward()