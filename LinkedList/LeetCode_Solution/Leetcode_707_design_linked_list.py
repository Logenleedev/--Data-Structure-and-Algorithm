class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        count = 0
        current = self.head
        while current != None:
            if(count == index):
                return current.data
            else:
                current = current.next
                count += 1 
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.size += 1
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            self.size += 1

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if self.size == 0:
            
            self.head = temp
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
            
            self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
            if index == 0:
                temp = self.head
                self.head = Node(val)
                self.head.next = temp
            else: 
                if index < self.size:

                    count = 0
                    current = self.head
                    while count < index:
                        if count == index - 1:
                            node = Node(val)
                            temp = current.next
                            current.next = node
                            node.next = temp
                            self.size += 1
                            count += 1
                        else:
                            current = current.next 
                            count += 1
                if index == self.size:
                    self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
            if index == 0:
                self.head = self.head.next
            else:            
                if index < self.size:
                    count = 0
                    current = self.head

                    while count <= index:
                        if count == index - 1:
                            
                            current.next = current.next.next
                            self.size -= 1
                            count += 1
                        else:
                            current = current.next 
                            count += 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)