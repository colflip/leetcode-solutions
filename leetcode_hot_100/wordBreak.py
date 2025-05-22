# 139. 单词拆分

from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)
