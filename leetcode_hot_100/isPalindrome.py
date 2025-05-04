# 234. 回文链表
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = slow.next
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True