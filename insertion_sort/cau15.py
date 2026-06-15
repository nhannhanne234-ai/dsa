class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def insertion_sort_linked_list(head):
    dummy = Node(0)
    while head:
        next_node = head.next
        prev = dummy
        while prev.next and prev.next.val < head.val:
            prev = prev.next
        head.next = prev.next
        prev.next = head
        head = next_node
    return dummy.next

node1 = Node(3)
node2 = Node(1)
node3 = Node(2)

node1.next = node2
node2.next = node3

sorted_head = insertion_sort_linked_list(node1)
print("Danh sách sau khi dùng Insertion Sort:")
current = sorted_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("null")