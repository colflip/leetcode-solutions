# 剑指 Offer 57.和为s的两个数字
# https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [nums[l], nums[r]]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []
