# 剑指 Offer 66. 构建乘积数组
# https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def constructArr(self, a) -> list:
        b = [1] * len(a)
        tmp = 1
        for i in range(1, len(a)):
            tmp *= a[i - 1]
            b[i] = tmp
        tmp = 1
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
            i -= 1
        return b


a = [1, 2, 3, 4, 5]
print(Solution().constructArr(a))
