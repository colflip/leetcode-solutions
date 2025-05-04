# 160. 相交链表

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a