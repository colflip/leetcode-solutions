# 剑指 Offer 48.最长不含重复字符的子字符串
# https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-chuan-lcof/description/?envType=problem-list-v2&envId=G25w0aD1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = temp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            temp = temp + 1 if temp < j - i else j - i
            res = max(res, temp)
        return res


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
