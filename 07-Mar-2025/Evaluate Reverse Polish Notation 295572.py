# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        a , b = 0 , 0
        for ch in tokens:
            if ch == '+':
                b = stk.pop()
                a = stk.pop()
                stk.append(a + b)
            elif ch == '*':
                b = stk.pop()
                a = stk.pop()
                stk.append(a * b)
            elif ch == '/':
                b = stk.pop()
                a = stk.pop()
                stk.append(int(a / b))
            elif ch == '-':
                b = stk.pop()
                a = stk.pop()
                stk.append(a - b)
            else:
                stk.append(int(ch))
        return stk[0]