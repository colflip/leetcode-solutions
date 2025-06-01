# 剑指 Offer 24. 反转链表
# https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        currNode = head
        while currNode:
            tmpNode = currNode.next
            currNode.next = preNode
            preNode = currNode
            currNode = tmpNode
        return preNode
