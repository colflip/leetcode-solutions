# 剑指 Offer 06. 从尾到头打印链表
# https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        reslist = []
        while head:
            reslist.append(head.val)
            head = head.next
        return reslist[::-1]
