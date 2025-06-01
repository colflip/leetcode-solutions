# 面试题61. 扑克牌中的顺子
# https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        numZeros = nums.count(0)
        if len(set(nums[numZeros:])) < len(nums[numZeros:]):
            return False
        return nums[-1] - nums[numZeros] <= 4
