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

    def deleteKthFromEnd(self, k):
        dummy = Node(0)
        dummy.next = self.head
        fast = dummy
        slow = dummy
        for _ in range(k):
            if fast.next is None:
                return
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        self.head = dummy.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("null")

lst = SinglyLinkedList()
for x in [1, 2, 3, 4, 5]:
    lst.pushBack(x)
lst.deleteKthFromEnd(2)
lst.display()