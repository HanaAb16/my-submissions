# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val = '' , next = None , prev = None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = Node(homepage)
        self.tail = self.browser

    def visit(self, url: str) -> None:
        new = Node(url)
        self.tail.next = new
        new.prev = self.tail
        self.tail = self.tail.next

    def back(self, steps: int) -> str:
        while self.tail.prev and steps > 0:
            self. tail = self.tail.prev
            steps -= 1
        return self.tail.val

    def forward(self, steps: int) -> str:
        while self.tail.next and steps > 0:
            self. tail = self.tail.next
            steps -= 1
        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)