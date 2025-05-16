# 152. 乘积最大子数组

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_val, min_val = res, res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_val, min_val = min_val, max_val
            max_val = max(nums[i], max_val * nums[i])
            min_val = min(nums[i], min_val * nums[i])
            res = max(res, max_val)
        return res
    