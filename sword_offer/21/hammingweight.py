# 剑指 Offer 15. 二进制中1的个数
# https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


n = 3
print(Solution().hammingWeight(n))
