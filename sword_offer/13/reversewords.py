# 剑指 Offer 58 - I. 翻转单词顺序
# https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = "the sky is blue"
print(Solution().reverseWords(s))
