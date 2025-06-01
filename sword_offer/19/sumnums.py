# 剑指 Offer 64. 求1+2+…+n
# https://leetcode.cn/problems/qiu-12n-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))


n = 3
print(Solution().sumNums(n))
