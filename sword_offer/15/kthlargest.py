# 剑指 Offer 54. 二叉搜索树的第k大节点
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.vals.append(node.val)
                inorder(node.right)

        inorder(root)
        return self.vals[len(self.vals) - k]
