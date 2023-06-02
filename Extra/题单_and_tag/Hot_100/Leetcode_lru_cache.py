class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}

        # least recent used 
        self.left = Node(0, 0)
        # most recent used 
        self.right = Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left 


    def remove(self, node):
        prev, nxt = node.prev,  node.next
        prev.next, nxt.prev = nxt, prev



    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node 
        node.prev = prev 
        node.next = self.right


    def get(self, key: int) -> int:
        if key in self.lru.keys():
            self.remove(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].value

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.lru.keys():
            self.remove(self.lru[key])

        self.lru[key] = Node(key, value)
        self.insert(self.lru[key])

        if len(self.lru.keys()) > self.capacity:
            target = self.left.next
            self.remove(self.left.next)
            del self.lru[target.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
