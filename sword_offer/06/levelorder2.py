# 剑指 Offer 32 - II. 从上到下打印二叉树 II
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/description/?envType=problem-list-v2&envId=G25w0aD1

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, q, this_row = [[root.val]], [root], []
        while q:
            while q:
                cur = q.pop(0)
                if cur.left:
                    this_row.append(cur.left)
                if cur.right:
                    this_row.append(cur.right)a
            if not this_row:
                return res
            q += this_row
            res.append([e.val for e in this_row])
            this_row = []
            
        return res
