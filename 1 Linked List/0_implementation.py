class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

linkedList = LinkedList()
linkedList.head = Node(1)
second = Node(2)
thrid = Node(3)
fourth = Node(4)

linkedList.head.next = second
second.next = thrid
thrid.next = fourth

temp = linkedList.head
while temp:
    print(temp.data)
    nextPtr = temp.next
    temp = nextPtr