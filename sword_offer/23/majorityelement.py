# 剑指 Offer 39. 数组中出现次数超过一半的数字
# https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def majorityElement(self, nums) -> int:
        return sorted(nums)[len(nums) // 2]


nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(Solution().majorityElement(nums))
