# 剑指 Offer 58 - II. 左旋转字符串
# https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


s = "abcdefg"
sol = Solution()
print(sol.reverseLeftWords(s, 2))
