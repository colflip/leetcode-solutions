# 494. 目标和
# https://leetcode.cn/problems/target-sum//description/?envType=problem-list-v2&envId=2cktkvj
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # 转换为子集和问题：sum(P) = (target + total) // 2
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        subset_sum = (target + total) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[subset_sum]
