#!/usr/bin/env python3

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
        self.size += 1
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode


    def dequeue(self):
        if self.isEmpty():
           return None
        dq = self.head
        self.head = self.head.next
        dq.next = None
        self.size -= 1
        return dq.data

    def front(self):
        return self.head

    def back(self):
        return self.tail

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def clear(self):
        self.head = None

    def isIn(self, data):
        current = self.head
        while current:
            if(data == current.data):
                return True
            current = current.next
        return false

    def getSize(self):
        return self.size

    def printQ(self):
        current = self.head
        if self.isEmpty():
            print("Queue Empty")
            return
        while current:
            print(current.data)
            current = current.next


q = Queue()
q.printQ()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# q.printQ()
# print(f"Dequeue: {q.dequeue()}")
# print(f"Size: {q.getSize()}")
