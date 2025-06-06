# 剑指 Offer 33. 二叉搜索树的后序遍历序列
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(nums):
            if len(nums) <= 1:
                return True
            root = nums[-1]
            for i in range(len(nums)):
                if nums[i] > root:
                    break
            for j in range(i, len(nums) - 1):
                if nums[j] < root:
                    return False
            return helper(nums[:i]) and helper(nums[i:-1])

        if not postorder:
            return True
        return helper(postorder)
