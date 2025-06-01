# 剑指 Offer 09. 用两个栈实现队列
# https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/description/?envType=problem-list-v2&envId=G25w0aD1


class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2 == []:
            if self.stack1 == []:
                return -1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
