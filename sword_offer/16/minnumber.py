# 面试题45. 把数组排成最小的数
# https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def minNumber(self, nums) -> str:
        return "".join(list(map(str, sorted(nums, key=lambda x: str(x) * 5))))
