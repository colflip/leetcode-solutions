# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii//description/?envType=problem-list-v2&envId=2cktkvj


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detect the start of the cycle in a linked list if it exists.
        :param head: The head of the linked list.
        :return: The node where the cycle begins, or None if there is no cycle.
        """
        slow = fast = head

        # First step: Determine if a cycle exists using Floyd's Tortoise and Hare algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        # Second step: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
