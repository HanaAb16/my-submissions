# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def dp(l , r):
            if s[l:r + 1] in wordDict and r == len(s):
                return True
            if r == len(s):
                return False
            if (l , r) not in memo:
                include = False
                if s[l:r + 1] in wordDict:
                    include = dp(l , r + 1) or dp(r + 1 , r + 1)
                exclude = dp(l , r + 1)
                memo[(l , r)] = include or exclude
            return memo[(l , r)]
        return dp(0 , 0)






        