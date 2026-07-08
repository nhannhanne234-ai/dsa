class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def findCycleStart(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3
lst = SinglyLinkedList()
lst.head = n1
start = lst.findCycleStart()
if start:
    print(f"điểm bắt đầu chu trình: {start.data}")
else:
    print("không chu trình")