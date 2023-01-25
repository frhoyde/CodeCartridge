#!/usr/bin/env python3

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def str(self):
        return f"Append: {self.data}"


class linkedList:
    def __init__(self):
        self.head = None
        self.listSize = 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.listSize += 1
            return None
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        self.listSize += 1
        print(newNode.str())


    def insertAt(self, position, data):
        newNode = Node(data)
        if position >= self.size():
            self.append(data)
        else:
            currPos = 0
            current = self.head
            while current:
                if(currPos == position-1):
                    newNode.next = current.next
                    current.next = newNode
                current = current.next
                currPos += 1



    def remove(self, data):
        current = self.head
        if(data == self.head.data):
            return self.removeFirst()
        while current.next:
            if(current.next.data == data):
                current.next = current.next.next
                return data
            current = current.next
            self.listSize -= 1
        return None

    def removeFirst(self):
        removedhead = self.head
        self.head = self.head.next
        removedhead.next = None
        self.listSize -= 1
        return removedhead.data



    def removeTail(self):
        current = self.head
        popped = None
        while current.next.next:
            current = current.next
        popped = current.next.data
        current.next = None
        return popped

    def isEmpty(self):
       if not self.head:
           return True
       else:
           return False

    def printList(self):
        current = self.head
        if not self.isEmpty():
            print(current.data)
            while current.next:
                current = current.next
                print(current.data)
        else:
            print("Empty List. Append some data to continue")

    def size(self):
        return self.listSize

    def find(self, data):
        current = self.head
        if self.isEmpty():
            return None
        position = 0
        while current:
            if(data == current.data):
                return position
            current = current.next
            position += 1
        return None

    def isIn(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def removeAllOf(self, data):
        current = self.head
        while current:
            if current.data == data:
                self.remove(data)
            current = current.next

    def reverseList(self):
        pass
ll = linkedList()
ll.printList()

ll.append(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.printList()
ll.insertAt(11, 3)
ll.printList()
ll.removeAllOf(3)
ll.printList()
# print(ll.isIn(11))
# print(f"Popped: {ll.removeTail()}")
# print(f"removed {ll.remove(2)}")
# ll.printList()
# print(f"removed Head: {ll.remove(1)}")
# ll.printList()
# print(f"Position of 3: {ll.find(3)}")
