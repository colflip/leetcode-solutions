# 剑指 Offer 17. 打印从1到最大的n位数
# https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


from typing import List


class Solution:
    def countNumbers(self, n: int) -> List[int]:
        out_list = list()
        for i in range(1, 10**n):
            out_list.append(i)
        return out_list
