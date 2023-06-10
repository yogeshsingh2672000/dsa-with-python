class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, node) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return
    
    # Iterative approach
    def countIterative(self) -> None:
        temp = self.head
        count = 0
        while temp:
            count += 1
            nextPtr = temp.next
            temp = nextPtr
        print(count)
        return count
    
    # recursive approach
    def countRecursive(self, head) -> None:
        if head == None:
            return 0
        return 1 + self.countRecursive(head.next)
        

linkedList = LinkedList()
linkedList.head = Node(1)
linkedList.push(Node(2))
linkedList.push(Node(3))
linkedList.push(Node(4))
linkedList.push(Node(5))


linkedList.countIterative()

linkedList.countRecursive(linkedList.head)