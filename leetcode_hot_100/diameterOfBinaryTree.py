# 543. 二叉树的直径
# https://leetcode.cn/problems/diameter-of-binary-tree/？envType=problem-list-v2&envId=2cktkvj
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter
