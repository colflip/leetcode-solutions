# 438. 找到字符串中的所有字母异位词
# httsps://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=2cktkvj
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        result = []

        for i in range(len(s)):
            s_count[s[i]] += 1

            if i >= len(p):
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    s_count[s[i - len(p)]] -= 1

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result
