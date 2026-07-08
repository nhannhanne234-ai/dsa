class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    tail = head
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    if head1:
        tail.next = head1
    else:
        tail.next = head2
    return head

a1 = Node(1)
a2 = Node(3)
a3 = Node(5)
a1.next = a2
a2.next = a3
b1 = Node(2)
b2 = Node(4)
b1.next = b2
merged = mergeSortedLists(a1, b1)