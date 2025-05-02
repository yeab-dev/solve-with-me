class ListNode:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        
        newNode = ListNode(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.previous = newNode

        else:
            newNode.next = self.head
            newNode.previous = self.tail

            self.head.previous = newNode
            self.tail.next= newNode

            self.head = newNode

        self.count += 1
        return True 

    def insertLast(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        
        newNode = ListNode(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        
        else:
            newNode.next = self.head
            newNode.previous = self.tail

            self.head.previous = newNode
            self.tail.next = newNode

            self.tail = newNode
        
        self.count += 1
        return True



    def deleteFront(self) -> bool:
        if not self.head:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            delNode = self.head
            self.head = delNode.next
            self.tail.next = self.head
            self.head.previous = self.tail
            delNode.next = None
        
        self.count -= 1
        return True


    def deleteLast(self) -> bool:
        if not self.tail:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            delNode = self.tail
            self.tail = delNode.previous
            
            self.tail.next = self.head
            self.head.previous = self.tail
            delNode.previous = None

        self.count -= 1
        return True

    def getFront(self) -> int:
        return self.head.value if self.head else -1
    def getRear(self) -> int:
        return self.tail.value if self.tail else -1

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        return self.count >= self.k