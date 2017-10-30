def insert(self, head, data):
    if head == None:
        return Node(data)
    else:
        if head.next == None:
            head.next = Node(data)
            return head
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
            return head
