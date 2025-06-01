# 剑指 Offer 63. 股票的最大利润
# https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/description/?envType=problem-list-v2&envId=G25w0aD1
# 遍历prices的过程中，维护一个最小值mins，并不断更新最大利润res的值
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        res = 0
        mins = prices[0]
        for i in range(1, len(prices)):
            mins = min(mins, prices[i])
            res = max(res, prices[i] - mins)
        return res


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
