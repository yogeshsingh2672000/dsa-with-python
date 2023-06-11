class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, node):
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
            temp.prev = prev
        temp.next = node
    
linkedList = LinkedList()
linkedList.head =  Node(1)
linkedList.push(Node(2))
linkedList.push(Node(3))
linkedList.push(Node(4))
linkedList.push(Node(5))

print("printing data using next pointer")
temp = linkedList.head
while temp:
    print(temp.data)
    temp = temp.next

    