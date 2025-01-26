from collections import deque

class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.stack_tmp = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack) != 0:
            self.stack_tmp.append(self.stack.pop())
        val = self.stack_tmp.pop()
        while len(self.stack_tmp) != 0:
            self.stack.append(self.stack_tmp.pop())
        return val

    def peek(self) -> int:
        while len(self.stack) != 0:
            self.stack_tmp.append(self.stack.pop())
        val = self.stack_tmp[-1]
        while len(self.stack_tmp) != 0:
            self.stack.append(self.stack_tmp.pop())
        return val

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()