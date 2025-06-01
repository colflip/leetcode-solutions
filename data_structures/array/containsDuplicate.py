# 217. 存在重复元素
# https://leetcode-cn.com/problems/contains-duplicate/


class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
