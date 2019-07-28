#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = 0
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.minimum = x
        else:
            self.minimum = min(self.minimum, x)
        self.stack.append(x)

    def pop(self) -> None:
        out = self.stack.pop()
        if out == self.minimum and self.stack:
            self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

