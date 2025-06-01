# 剑指 Offer 56 - II. 数组中数字出现的次数 II
# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def singleNumber(self, nums) -> int:
        print(nums)
        print(list(set(nums)))
        return (3 * sum(list(set(nums))) - sum(nums)) // 2


nums = [3, 4, 3, 3]
print(Solution().singleNumber(nums))
