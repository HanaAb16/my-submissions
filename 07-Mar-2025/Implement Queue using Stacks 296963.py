# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        stack2 = list(reversed(self.stack1))
        a = stack2.pop()
        self.stack1 = list(reversed(stack2))
        return a
    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if self.stack1:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()