# 739. 每日温度
# https://leetcode.cn/problems/daily-temperatures//description/?envType=problem-list-v2&envId=2cktkvj

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
