# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: {(0, -1), (0, 1)},
            2: {(-1, 0), (1, 0)},
            3: {(0, -1), (1, 0)},
            4: {(0, 1), (1, 0)},
            5: {(0, -1), (-1, 0)},
            6: {(0, 1), (-1, 0)}
        }
        
        queue = deque([(0, 0)])
        end = (len(grid) - 1, len(grid[0]) - 1)
        isbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set()
        while queue:
            i, j = queue.popleft()
            visited.add((i , j))
            if (i , j) == end:
                return True
            for row,  col in directions[grid[i][j]]:
                newr, newc = i + row, j + col

                if isbound(newr, newc) and (-1 * row, -1 * col) in directions[grid[newr][newc]] and (newr, newc) not in visited:
                    queue.append((newr, newc))
        
        return False