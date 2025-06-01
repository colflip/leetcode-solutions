# 剑指 Offer 38. 字符串的排列
# https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = [""]
        for c in s:
            ans = [
                word[:i] + c + word[i:]
                for word in ans
                for i in range((word + c).index(c) + 1)
            ]
        return ans
