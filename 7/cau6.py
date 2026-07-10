class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def question_six(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p = head
            while p != slow:
                p = p.next
                slow = slow.next
            return p
    return None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

start = question_six(a)
if start:
    print(start.value)