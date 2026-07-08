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

    def merge(self, left, right):
        dummy = Node(0)
        tail = dummy
        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        else:
            tail.next = right
        return dummy.next
    
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(mid)
        return self.merge(left, right)
    
    def sort(self):
        self.head = self.mergeSort(self.head)

lst = SinglyLinkedList()

lst.pushBack(3)
lst.pushBack(1)
lst.pushBack(2)
lst.pushBack(5)
lst.pushBack(4)

lst.display()
lst.sort()
lst.display()