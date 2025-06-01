# 238. 除自身以外数组的乘积
# https://leetcode.cn/problems/product-of-array-except-self//description/?envType=problem-list-v2&envId=2cktkvj

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
