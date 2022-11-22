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

    def push_back(self, new_data): # Adding an element after the last element
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None: # checks whether the list is empty, if so make both head and tail as new node
            self.head = new_node 
            self.tail = new_node
            new_node.next = None # the first element's previous pointer has to refer to null
                
        else: # If list is not empty, change pointers accordingly
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node 

    def peek_front(self): # returns first element
        if self.head == None and self.tail == None: 
            print("Nothing is here")
        else:
            return self.head.data
    
    def peek_back(self): # returns last element
        if self.head == None and self.tail == None: 
            print("Nothing is here")
        else:
            return self.tail.data

    def pop_front(self): # removes and returns the first element
        if self.head == None: 
            print("Cannot pop since the list is empty")
            return None
        else:
            self.head.next.prev = None
            self.head = self.head.next
            
            return self.head.data
    

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
    L.push_front(6)
    L.push_front(5)
    L.push_front(3)
    L.pop_front()
    L.pop_front()
    L.printLinkedList()