# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path , opening , closing):
            if closing == 0:
                ans.append(path)
                return
            if opening == 0:
                backtrack(path + ')' , opening , closing - 1)
            elif opening < closing:
                backtrack(path + ')' , opening , closing - 1)
                backtrack(path + '(' , opening - 1 , closing)
            if opening == closing:
                backtrack(path + '(' , opening - 1 , closing)
            
            return
        backtrack('' , n , n)
        return ans
