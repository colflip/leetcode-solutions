# 面试题59 - II. 队列的最大值
# https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


import queue


class MaxQueue:
    def __init__(self):
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1
