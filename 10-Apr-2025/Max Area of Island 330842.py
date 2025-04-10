# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        def inBound(r , c):
            return 0 <= r < m and 0 <= c < n
        def dfs(row , col):
            area = 0
            grid[row][col] = 0
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if inBound(new_row , new_col) and grid[new_row][new_col]:
                    grid[new_row][new_col] = 0
                    area += dfs(new_row , new_col)
            return area + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(dfs(i , j) , ans)
        return ans

