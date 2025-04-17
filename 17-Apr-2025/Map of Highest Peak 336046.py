# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        directions = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        inbound = lambda a , b : 0 <= a < n and 0 <= b <m
        height = [[-1] * m for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i , j))
        if not queue:
            queue.append((0 , 0))

        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for d in directions:
                    newr = r + d[0]
                    newc = c + d[1]
                    if inbound(newr , newc) and height[newr][newc] == -1:
                        height[newr][newc] = height[r][c] + 1
                        queue.append((newr , newc))
        return height
