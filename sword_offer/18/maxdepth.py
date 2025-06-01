# 剑指 Offer 55 - I. 二叉树的深度
# https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


root = [3, 9, 20, None, None, 15, 7]
temp_node = head_node = left_node = TreeNode(root[0])
temp_node.left = None
for i in root[1:]:
    node = left_node = TreeNode(i)
    temp_node.left = left_node
    temp_node.right = node
    temp_node = temp_node.right
print(Solution().maxDepth(head_node))
