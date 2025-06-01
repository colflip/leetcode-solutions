# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def missingNumber(self, nums) -> int:
        sum = int((len(nums)) * (1 + len(nums)) / 2)
        tem = 0
        for i in nums:
            tem = tem + i
        return sum - tem


nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
print(Solution().missingNumber(nums))
