class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_selection_sort(head: Node) -> Node:
    if not head or not head.next:
        return head
    dummy = Node(0)
    tail = dummy
    current = head
    while current:
        min_node = current
        min_prev = None
        run_prev = current
        run = current.next
        while run:
            if run.data < min_node.data:
                min_node = run
                min_prev = run_prev
            run_prev = run
            run = run.next
        if min_node == current:
            current = current.next
        else:
            min_prev.next = min_node.next
        tail.next = min_node
        tail = min_node
        tail.next = None
    return dummy.next

def print_list(head: Node):
    res = []
    while head:
        res.append(str(head.data))
        head = head.next
    print(" -> ".join(res) + " -> null")

head = Node(3); head.next = Node(1); head.next.next = Node(2)
sorted_head = linked_list_selection_sort(head)
print_list(sorted_head)