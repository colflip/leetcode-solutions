# 剑指 Offer 38. 字符串的排列
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = ['']
        for c in s:
            ans = [word[:i] + c + word[i:] for word in ans for i in range((word + c).index(c) + 1)]
        return ans
