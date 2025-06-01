# 215. 数组中的第K个最大元素
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums))
