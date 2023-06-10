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
    
    def printList(self) -> None:
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        return
    
    def deleteFromStart(self) -> None:
        temp = self.head
        if temp.next:
            newHead = temp.next
            self.head = newHead
        return
    
    def deleteFromEnd(self) -> None:
        temp = self.head
        while temp.next:
            if temp.next.next == None:
                temp.next = None
            else:
                temp = temp.next
        return
    
    def deleteByKey(self, position) -> None:
        temp = self.head

        # if position is 1 mean deletion from start
        if position == 1:
            self.deleteFromStart()
            return
        
        count = 1
        while temp.next:
            if position == (count + 1):
                temp.next = temp.next.next
                return
            else:
                temp= temp.next
                count += 1        
        return

linkedList = LinkedList()
linkedList.head = Node(1)
linkedList.push(Node(2))
linkedList.push(Node(3))
linkedList.push(Node(4))
linkedList.push(Node(5))

print("deleting from start")
linkedList.deleteFromStart()
linkedList.printList()

print("deleting from End")
linkedList.deleteFromEnd()
linkedList.printList()

print("deleting from a position")
linkedList.deleteByKey(5)
linkedList.printList()