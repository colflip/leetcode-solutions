# 461. 汉明距离
# https://leetcode.cn/problems/hamming-distance//description/?envType=problem-list-v2&envId=2cktkvj


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
