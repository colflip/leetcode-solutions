# 剑指 Offer 32 - I. 从上到下打印二叉树
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#


class Solution:
    def levelOrder(self, root):
        temp = [root]
        ans = []
        while len(temp) > 0:
            if temp[0] is not None:
                ans.append(temp[0].val)
                temp.append(temp[0].left)
                temp.append(temp[0].right)

            temp.pop(0)
        return ans
