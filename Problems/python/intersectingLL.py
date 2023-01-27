#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB
        while currentA != currentB:
            currentA = [headB if not currentA else currentA.next]
            currentB = [headA if not currentB else currentB.next]
        return currentA
sol = Solution()
sol.getIntersectionNode([4,1,8,4,5], [5,6,1,8,4,5])
