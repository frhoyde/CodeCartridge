#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        pos = 0
        sum = 0
        while current1:
            sum += current1.val * (10 ** pos)
            pos += 1
            current1 = current1.next
        pos = 0
        while current2:
            sum += current2.val * (10**pos)
            pos += 1
            current2 = current2.next
        tmp = sum % 10
        sum = sum // 10
        newHead = ListNode(tmp)
        current = newHead
        while sum != 0:
            tmp = sum % 10
            sum = sum // 10
            newNode = ListNode(tmp)
            current.next = newNode
            current = current.next
        return newHead
