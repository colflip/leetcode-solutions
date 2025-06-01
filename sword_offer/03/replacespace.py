# 剑指 Offer 05. 替换空格
# https://leetcode.cn/problems/ti-huan-kong-ge-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


s = "We are happy."
sol = Solution()
print(sol.replaceSpace(s))
