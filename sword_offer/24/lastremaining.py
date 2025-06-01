# 剑指 Offer 62. 圆圈中最后剩下的数字
# https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        p = 0
        for i in range(2, n + 1):
            p = (p + m) % i
        return p


if __name__ == "__main__":
    n, m = 70866, 116922
    solution = Solution()
    print(solution.lastRemaining(n, m))
