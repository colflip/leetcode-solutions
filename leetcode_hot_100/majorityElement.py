# 169. 多数元素
# https://leetcode.cn/problems/majority-element//description/?envType=problem-list-v2&envId=2cktkvj


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
