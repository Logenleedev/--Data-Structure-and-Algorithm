class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def setData(self, data):
        self.data = data
    
    def getdata(self):
        return self.data

    def setnext(self, next):
        self.next = next
    
    def getnext(self):
        return self.next

    



class LinkedList:
    def __init__(self):
        self.head = None

    def insertFront(self, data):
        if (self.head == None):
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
    
    def printLinkedList(self):
        if (self.head == None):
            print("Nothing here")
        else:
            temp = self.head
            while (temp != None):
                print("{}".format(temp.data))
                temp = temp.next
    
    def insertBack(self, data):
        temp = self.head

        while(temp.next != None):
            temp = temp.next
        
        node = Node(data)
        temp.next = node

    def insertBetween(self, preNode, data):
        node = Node(data)
        if self.head == None:
            print("Operation not allowed since the next Node does not exist")
        else:
            temp = self.head
            while(temp.data != preNode.data):
                temp = temp.next
            
            swap = temp.next
            temp.next = node
            node.next = swap

if __name__ == "__main__":
    L = LinkedList()
    L.insertFront(4)
    L.insertFront(3)
    L.insertFront(3)
    L.insertFront(5)
    L.insertBetween(Node(3), 20)
    L.printLinkedList()

