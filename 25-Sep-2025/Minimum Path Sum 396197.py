# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        def inbound(r , c): return 0 <= r < n and 0 <= c < m
        memo = {}
        def dp(i , j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if (i , j) not in memo:
                val1 , val2 = inf , inf
                if inbound(i + 1 , j):
                    val1 = dp(i + 1 , j)
                if inbound(i , j + 1):
                    val2 = dp(i , j + 1)
                memo[(i , j)] = grid[i][j] + min(val1 , val2)
            return memo[(i , j)]
        return dp(0 , 0)
