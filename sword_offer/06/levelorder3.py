# 剑指 Offer 32 - III. 从上到下打印二叉树 III
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/description/?envType=problem-list-v2&envId=G25w0aD1

import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, deque = [], collections.deque([root])
        while deque:
            temp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(temp))
        return res
