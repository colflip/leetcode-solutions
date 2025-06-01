# 剑指 Offer 35. 复杂链表的复制
# https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]
