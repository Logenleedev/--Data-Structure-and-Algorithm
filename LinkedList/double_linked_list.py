# Creating a node class
class Node:
  def __init__(self, data):
    self.data = data #adding an element to the node
    self.next = None # Initally this node will not be linked with any other node
    self.prev = None # It will not be linked in either direction


# Creating a doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None # Initally there are no elements in the list
        self.tail = None

    def push_front(self, data): # Adding an element before the first element
        node = Node(data)
        node.next = self.head

        if self.head != None:
            self.head.prev = node
            self.head = node
            self.head.prev = None
        else:
            self.head = node
            self.head.prev = None
            self.head.next = None

    def printLinkedList(self):
        if (self.head == None):
            print("Nothing here")
        else:
            temp = self.head
            while (temp != None):
                print("{}".format(temp.data))
                temp = temp.next

if __name__ == "__main__":
    L = DoublyLinkedList()
    L.push_front(5)
    L.push_front(3)
    L.printLinkedList()