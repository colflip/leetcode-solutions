# 剑指 Offer 03. 数组中重复的数字
# https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict:
                return i
            else:
                dict[i] = 1
        return -1


nums = [2, 3, 1, 0, 2, 5, 3]
print(Solution().findRepeatNumber(nums))
