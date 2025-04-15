# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        def inBound(row , col):
            return 0 <= row < n and 0 <= col < m
        rotten = []
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i , j)) 
                    count += 1
                if grid[i][j] == 1:
                    count += 1
        queue = deque(rotten)
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                count -= 1
                for d in directions:
                    newr = r + d[0]
                    newc = c + d[1]
                    if inBound(newr , newc) and grid[newr][newc] == 1:
                        queue.append((newr , newc))
                        grid[newr][newc] = 2
            ans += 1
        if count != 0:
            return -1
        if ans == 0:
            return 0
        return ans - 1
           
            


