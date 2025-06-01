# 剑指 Offer 40. 最小的k个数
# https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def getLeastNumbers(self, arr, k: int):
        return sorted(arr)[:k]


arr = [3, 2, 1]
k = 2
print(Solution().getLeastNumbers(arr, k))
