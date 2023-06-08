class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, node):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        return

linkedList = LinkedList()
linkedList.head = Node(1)
linkedList.push(Node(2))
linkedList.push(Node(3))
linkedList.push(Node(4))

curr = linkedList.head
while curr.next:
    print(curr.data)
    nextPtr = curr.next
    curr = nextPtr
