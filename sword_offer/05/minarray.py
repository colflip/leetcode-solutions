# 剑指 Offer 11. 旋转数组的最小数字
# https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def minArray(self, numbers) -> int:
        temp = numbers[0]
        for i in numbers:
            if i < temp:
                return i
        return temp

        # -------------------------------
        # return min(numbers)


numbers = [3, 4, 5, 1, 2]
print(Solution().minArray(numbers))
