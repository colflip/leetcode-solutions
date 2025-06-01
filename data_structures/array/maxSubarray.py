# 53. 最大子数组和
# https://leetcode-cn.com/problems/maximum-subarray/


class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)
