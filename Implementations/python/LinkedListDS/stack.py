#!/usr/bin/env python3

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def pushFront(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode


    def popFront(self):
        currentHead = self.head
        if self.isEmpty():
            return None
        self.head = currentHead.next
        currentHead.next = None
        return currentHead.data

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    def printStack(self):
        current = self.head
        if self.isEmpty():
            print("Empty Stack. Push Data to continue")
            return
        while current:
            print(current.data)
            current = current.next

s = Stack()
s.printStack()
# s.pushFront(1)
# s.pushFront(2)
# s.pushFront(3)
# s.pushFront(4)
# s.printStack()
# print(f"Popped: {s.popFront()}")
# s.printStack()
