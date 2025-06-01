# 283. 移动零
# https://leetcode.cn/problems/move-zeroes//description/?envType=problem-list-v2&envId=2cktkvj


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
