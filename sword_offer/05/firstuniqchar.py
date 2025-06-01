# 剑指 Offer 50. 第一个只出现一次的字符
# https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = Counter(s)
        for i in s:
            if counter[i] == 1:
                return i

        return " "


s = "abaccdeff"
print(Solution().firstUniqChar(s))
