class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return
    
    def searchIterative(self, data):
        temp = self.head
        while temp.next:
            if temp.data == data:
                return "Found"
            temp = temp.next
        return "Not found!"
    
    def searchRecursive(self, head, data):
        if head == None:
            return "Not found!"
        
        if head.data == data:
            return "Found"
        return self.searchRecursive(head.next, data)


linkedList = LinkedList()
linkedList.head = Node(1)
linkedList.push(Node(2))
linkedList.push(Node(3))
linkedList.push(Node(4))


print(linkedList.searchIterative(3))
# for searching in recursive you need to give head as a parameter
# or you can find another way around
print(linkedList.searchRecursive(linkedList.head, 3))