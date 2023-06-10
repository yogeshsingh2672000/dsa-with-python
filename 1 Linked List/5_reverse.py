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
    
    def reverse(self) -> None:
        temp = self.head
        prev = None
        while temp:
            currNext = temp.next
            temp.next = prev
            prev = temp
            temp = currNext
        self.head = prev
        return

    def printList(self, head) -> None:
        while head:
            print(head.data)
            head = head.next
        return

linkedList = LinkedList()
linkedList.head = Node(1)
linkedList.push(Node(2))
linkedList.push(Node(3))
linkedList.push(Node(4))
linkedList.push(Node(5))

linkedList.reverse()
linkedList.printList(linkedList.head)