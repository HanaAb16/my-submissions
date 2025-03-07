# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        ans = 0
        for par in s:
            if par == '(':
                stk.append(par)
            else:
                if stk[-1] == '(':
                    stk.pop()
                    stk.append(1)
                else:
                    temp = stk.pop()
                    while stk and stk[-1] != '(':
                        temp += stk.pop()
                    stk.pop()
                    stk.append(temp * 2)



                        
        return sum(stk)
