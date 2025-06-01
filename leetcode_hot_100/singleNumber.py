# 136. 只出现一次的数字
# https://leetcode.cn/problems/single-number//description/?envType=problem-list-v2&envId=2cktkvj

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
