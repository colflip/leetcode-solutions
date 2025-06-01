# 128. 最长连续序列
# https://leetcode.cn/problems/longest-consecutive-sequence//description/?envType=problem-list-v2&envId=2cktkvj


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num
                cur_res = 1
                while cur + 1 in nums:
                    cur += 1
                    cur_res += 1
                res = max(res, cur_res)
        return res
