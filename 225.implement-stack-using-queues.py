#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue1 = deque()
        self.queue2 = deque()
    
    def move_items(self):
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())
    
    def swap_queues(self):
        self.queue1, self.queue2 = self.queue2, self.queue1
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.move_items()
        item = self.queue1.popleft()
        self.swap_queues()
        return item
        

    def top(self) -> int:
        """
        Get the top element.
        """
        self.move_items()
        item = self.queue1.popleft()
        self.swap_queues()
        self.queue1.append(item)
        return item
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

