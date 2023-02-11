链表的基础操作：


```python
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
        cur = self.head 

        while cur:
            if count == index:
                return cur.data
            cur = cur.next 
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
                node = Node(val)
                node.next = self.head 
                self.head = node
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

                    while count < index:
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
```

链表的 while 后面的条件：
```
1. 只需要判断什么时候终止我们的遍历
2. 判断特殊情况
3. 根据 .next 的个数确定
```
案例：

唤醒链表 while 后面的 condition 是：
```
while fast and fast.next:
```


什么时候考虑用dummyhead？
```
一般来讲只要涉及到处理链表中node的情况（比如删除什么的）就可以考虑使用dummyhead。这样可以防止处理其他node的逻辑不一样。统一和简化代码。
```


链表的边界条件：
- 空链表：head 为 none
- 开头
- 结尾
  

