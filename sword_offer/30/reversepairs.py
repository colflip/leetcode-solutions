# 剑指 Offer 51. 数组中的逆序对
# https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for v in nums:
            i = bisect.bisect_left(q, -v)
            res += i
            q[i:i] = [-v]
        return res


nums = [7, 5, 6, 4]
print(Solution().reversePairs(nums))
