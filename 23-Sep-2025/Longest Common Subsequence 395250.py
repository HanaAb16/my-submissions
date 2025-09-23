# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n , m = len(text1) , len(text2)
        memo = {}
        def dp(i , j):
            if i == n or j == m:
                return 0
            include , exclude = 0 , 0
            if (i , j) not in memo:
                if text1[i] == text2[j]:
                    include = 1 + dp(i + 1 , j + 1)
                exclude = max(dp(i + 1 , j) , dp(i , j + 1))
                memo[(i , j)] = max(include , exclude)
            return memo[(i , j)]
        return dp(0 , 0)