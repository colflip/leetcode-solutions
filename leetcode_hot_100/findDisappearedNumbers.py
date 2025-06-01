# 448. 找到所有数组中消失的数字
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array//description/?envType=problem-list-v2&envId=2cktkvj


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
