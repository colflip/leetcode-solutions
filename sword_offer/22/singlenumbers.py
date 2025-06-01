# 剑指 Offer 56 - I. 数组中数字出现的次数
# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
            else:
                res.remove(i)
        return list(res)
