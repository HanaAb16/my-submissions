# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1 , stk2 = [] , []
        for ch in s:
            if ch == '#':
                if stk1:
                    stk1.pop()
            else:
                stk1.append(ch)
        for ch in t:
            if ch == '#':
                if stk2:
                    stk2.pop()
            else:
                stk2.append(ch)
        if stk1 == stk2:
            return True
        else:
            return False
            