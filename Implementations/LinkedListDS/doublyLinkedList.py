#!/usr/bin/env python3

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class linkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return None
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current
        return None

    def remove(self, data):
        current = self.head
        if(data == self.head.data):
            return self.removeFirst()
        while current:
            if(current.data == data):
                current.prev.next = current.next
                current.next.prev = current.prev
                current = None
                return data
            current = current.next
        return None

    def removeFirst(self):
        removedhead = self.head
        self.head = self.head.next
        self.head.prev = None
        popped = removedhead.data
        removedhead = None
        return popped

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


    def printListReverse(self):
        current = self.head
        if not self.isEmpty():
            while current.next:
                current = current.next
            while current:
                print(current.data)
                current = current.prev
        else:
            print("Empty List. Append some data to continue")

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

ll = linkedList()
ll.printList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# ll.printList()
# print("reverse: ")
# ll.printListReverse()
# ll.removeFirst()
# ll.printList()
# ll.removeTail()
# ll.printList()
