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

def addTwoNumbers(l1, l2):
    dummy = Node(0)
    tail = dummy
    carry = 0
    while l1 or l2 or carry:
        x = l1.data if l1 else 0
        y = l2.data if l2 else 0
        total = x + y + carry
        carry = total // 10
        tail.next = Node(total % 10)
        tail = tail.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next

def display(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next
    print("null")

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
display(l1)
display(l2)
result = addTwoNumbers(l1, l2)
display(result)