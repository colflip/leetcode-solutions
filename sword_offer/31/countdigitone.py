# 剑指 Offer 31. 数字 1 的个数
# https://leetcode.cn/problems/number-of-digit-one/description/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        t = 1
        for i in range(len(str(n)) - 1, 0, -1):
            num = 10**i
            a = n // num
            if a > t:
                ans += num
            elif a == t:
                ans += n - num + 1
            while n > num:
                ans += i * num // 10
                n -= num
        return ans + (n >= t)
