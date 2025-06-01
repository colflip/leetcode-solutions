# 剑指 Offer 14- I. 剪绳子
# https://leetcode.cn/problems/jian-sheng-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * (n % 3 + 3)
        else:
            return 3 ** (n // 3) * (n % 3)


n = 10
print(Solution().cuttingRope(n))
