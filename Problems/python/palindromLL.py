#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next is not None:
            # This traverses the linked list to find the middle of the list, the fast pointer goes 2x towards the end so when it does, the slow pointer gets to the middle
            slow = slow.next
            fast = fast.next.next
        reverseHead =None
        while slow:
            # This is standard linked list reversing
            next = slow.next
            slow.next = reverseHead
            reverseHead = slow
            slow = next
        while reverseHead:
            # This checks the reverse list is equal to the first half or not
            if reverseHead.val != head.val:
                return False
            reverseHead = reverseHead.next
            head = head.next
        return True
